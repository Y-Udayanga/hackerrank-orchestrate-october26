"""Loopback-only browser interface for the existing audit CLI."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import csv
import json
import secrets
import subprocess
import sys
import threading

ROOT = Path(__file__).resolve().parents[1]
TOKEN = secrets.token_urlsafe(32)
LOCK = threading.Lock()
STATE = {"running": False, "message": "Ready. Showing the latest saved audit.", "exit_code": None}

HTML = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GhostTrace AI</title><style>
*{box-sizing:border-box}body{margin:0;background:#0c1322;color:#e7edf7;font:15px system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:44px 24px}header{display:flex;align-items:center;justify-content:space-between;gap:24px}h1{font-size:34px;margin:8px 0}h2{font-size:20px}.eyebrow{color:#5eead4;letter-spacing:3px;font-size:12px}p{color:#a8b6cc;line-height:1.6}button,a.download{background:#5eead4;color:#082324;border:0;border-radius:8px;padding:12px 18px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-block}button:disabled{opacity:.5;cursor:wait}a{color:#5eead4}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:30px 0}.card,section{background:#131e31;border:1px solid #26344b;border-radius:12px;padding:20px}.card strong{display:block;font-size:32px;margin-top:8px}.card span{color:#a8b6cc}.toolbar{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}input,select{background:#0c1322;color:#e7edf7;border:1px solid #40506c;padding:12px;border-radius:8px}input{flex:1;min-width:180px}table{width:100%;border-collapse:collapse;text-align:left}td,th{padding:13px 10px;border-bottom:1px solid #26344b}th{color:#a8b6cc;font-size:12px;text-transform:uppercase}td button{padding:7px 12px;background:#263c53;color:#c7f9ed}.pill{font-size:12px;color:#fbbf24}.COMPLETE{color:#5eead4}.NOT_APPLICABLE{color:#a8b6cc}#status{padding:16px;background:#192942;border-radius:8px;margin:20px 0}dialog{background:#131e31;color:#e7edf7;border:1px solid #40506c;border-radius:12px;max-width:1100px;width:95%;max-height:85vh}dialog::backdrop{background:#000a}.scroll{overflow:auto}.empty{padding:30px;color:#a8b6cc}@media(max-width:650px){header{display:block}.cards{grid-template-columns:repeat(2,1fr)}main{padding:24px 14px}h1{font-size:28px}}
</style><main><header><div><div class="eyebrow">EVIDENCE-DRIVEN DELETION AUDITOR</div><h1>GhostTrace AI</h1><p>Trace remaining data. Inspect evidence. Plan safe remediation.</p></div><button id="run">Run full audit</button></header>
<div id="status" role="status">Loading saved results…</div><p>Runs all 518 requests using your configured Gemini access. API charges may apply. The audit produces a plan; it does not delete source data.</p>
<div class="cards"><div class="card"><span>Total cases</span><strong id="total">—</strong></div><div class="card"><span>Complete</span><strong id="complete">—</strong></div><div class="card"><span>Incomplete</span><strong id="incomplete">—</strong></div><div class="card"><span>Not applicable</span><strong id="na">—</strong></div></div>
<section><h2>Audit results</h2><p>Saved predictions may contain investigation gaps. A completed run does not guarantee that every deletion has been resolved.</p><div class="toolbar"><input id="search" placeholder="Search case ID" aria-label="Search case ID"><select id="filter" aria-label="Filter status"><option value="">All statuses</option><option>INCOMPLETE</option><option>COMPLETE</option><option>NOT_APPLICABLE</option></select><a class="download" href="/output.csv">Download CSV</a></div><div class="scroll"><table><thead><tr><th>Case</th><th>Status</th><th>Plan steps</th><th>Details</th></tr></thead><tbody id="rows"></tbody></table></div><p id="count"></p></section>
<dialog id="detail"><button id="close">Close</button><h2 id="title"></h2><div class="scroll"><table><thead><tr><th>#</th><th>Phase</th><th>System</th><th>Resource</th><th>Operation</th><th>State</th><th>Evidence</th></tr></thead><tbody id="steps"></tbody></table></div><p id="nosteps"></p></dialog></main>
<script>
const token='__TOKEN__';let data=[];const el=id=>document.getElementById(id);function cell(row,text){const td=document.createElement('td');td.textContent=text;row.append(td);return td}
function render(){const rows=data.filter(r=>r.case_id.toLowerCase().includes(el('search').value.toLowerCase())&&(!el('filter').value||r.deletion_status===el('filter').value));el('rows').replaceChildren();for(const r of rows){const tr=document.createElement('tr');cell(tr,r.case_id);cell(tr,r.deletion_status).className='pill '+r.deletion_status;cell(tr,r.steps.length);const b=document.createElement('button');b.textContent='View plan';b.onclick=()=>show(r);cell(tr,'').append(b);el('rows').append(tr)}el('count').textContent=`${rows.length} of ${data.length} cases`;}
function show(r){el('title').textContent=r.case_id+' · '+r.deletion_status;el('steps').replaceChildren();for(const s of r.steps){const tr=document.createElement('tr');for(const k of ['step_no','phase','system_id','resource_id','operation','state','evidence_id'])cell(tr,s[k]||'—');el('steps').append(tr)}el('nosteps').textContent=r.steps.length?'':(r.deletion_status==='NOT_APPLICABLE'?'No deletion authorized.':'No supported steps available; investigate the evidence gap.');el('detail').showModal()}
async function refresh(){try{const response=await fetch('/api/status');if(!response.ok)throw Error('Server unavailable');const s=await response.json();el('status').textContent=s.message;el('run').disabled=s.running;el('run').textContent=s.running?'Audit running…':'Run full audit';const res=await fetch('/api/results');if(!res.ok)throw Error('Cannot load results');data=await res.json();el('total').textContent=data.length;for(const [id,status] of [['complete','COMPLETE'],['incomplete','INCOMPLETE'],['na','NOT_APPLICABLE']])el(id).textContent=data.filter(r=>r.deletion_status===status).length;render()}catch(e){el('status').textContent=e.message+'. Check that the local server is running.'}}
el('run').onclick=async()=>{el('run').disabled=true;try{const r=await fetch('/api/run',{method:'POST',headers:{'X-GhostTrace-Token':token}});const s=await r.json();el('status').textContent=s.message}catch(e){el('status').textContent='Could not start audit.'}await refresh()};el('search').oninput=render;el('filter').onchange=render;el('close').onclick=()=>el('detail').close();refresh();setInterval(refresh,5000);
</script></html>'''


def run_audit():
    try:
        # Output is deliberately not served: provider exceptions may contain secrets.
        result = subprocess.run([sys.executable, str(ROOT / 'code/main.py')], cwd=ROOT,
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                timeout=3600)
        message = ('Audit finished. Saved results have been refreshed.' if result.returncode == 0 else
                   'Audit failed. Previous results are preserved. Run code/main.py in your terminal for diagnostics.')
        code = result.returncode
    except Exception:
        message, code = 'Audit could not finish. Check your local Python environment and Gemini configuration.', -1
    with LOCK:
        STATE.update(running=False, message=message, exit_code=code)


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, content_type='application/json; charset=utf-8'):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.end_headers()
        self.wfile.write(body)

    def valid_host(self):
        return self.headers.get('Host') in {'localhost:8000', '127.0.0.1:8000'}

    def do_GET(self):
        if not self.valid_host():
            return self.respond(403, {'message': 'Local access only.'})
        if self.path == '/':
            return self.respond(200, HTML.replace('__TOKEN__', TOKEN), 'text/html; charset=utf-8')
        if self.path == '/api/status':
            with LOCK:
                return self.respond(200, dict(STATE))
        if self.path in {'/api/results', '/output.csv'}:
            path = ROOT / 'output.csv'
            if self.path == '/output.csv':
                return self.respond(200, path.read_bytes(), 'text/csv; charset=utf-8') if path.exists() else self.respond(404, {'message': 'Run an audit first.'})
            try:
                with path.open(encoding='utf-8', newline='') as stream:
                    rows = [{'case_id': r['case_id'], 'deletion_status': r['deletion_status'],
                             'steps': json.loads(r['steps_json'])} for r in csv.DictReader(stream)]
            except FileNotFoundError:
                rows = []
            return self.respond(200, rows)
        self.respond(404, {'message': 'Not found.'})

    def do_POST(self):
        if not self.valid_host() or not secrets.compare_digest(self.headers.get('X-GhostTrace-Token', ''), TOKEN):
            return self.respond(403, {'message': 'Request rejected. Reload the local app.'})
        if self.path != '/api/run':
            return self.respond(404, {'message': 'Not found.'})
        with LOCK:
            if STATE['running']:
                return self.respond(409, {'message': 'An audit is already running.'})
            STATE.update(running=True, message='Auditing evidence with Gemini. This can take several minutes.', exit_code=None)
            threading.Thread(target=run_audit, daemon=True).start()
        self.respond(202, {'message': 'Audit started.'})


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8000), Handler)
    print('GhostTrace AI: http://localhost:8000 (Ctrl+C to stop)', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
