import base64,os
D='/home/claude/tools/node_modules/devicon/icons/'
def ic(n,f):
    p=D+n+'/'+f; return 'data:image/svg+xml;base64,'+base64.b64encode(open(p,'rb').read()).decode()
cats=[
 ("01","Backend",[("Java",ic('java','java-plain.svg'),1),("Spring Boot",ic('spring','spring-original.svg'),1),("Go",ic('go','go-plain.svg'),1),("Node.js",ic('nodejs','nodejs-plain.svg'),0)]),
 ("02","Architecture & APIs",[("REST",None,0),("GraphQL",ic('graphql','graphql-plain.svg'),0),("SOAP",None,0),("Hexagonal",None,0)]),
 ("03","Data",[("Oracle",ic('oracle','oracle-original.svg'),0),("PostgreSQL",ic('postgresql','postgresql-plain.svg'),0),("MySQL",ic('mysql','mysql-original.svg'),0),("SQL Server",ic('microsoftsqlserver','microsoftsqlserver-plain.svg'),0)]),
 ("04","Persistence & Build",[("Hibernate",ic('hibernate','hibernate-plain.svg'),0),("MyBatis",None,0),("Maven",ic('maven','maven-plain.svg'),0),("JSF",None,0)]),
 ("05","Platform",[("Docker",ic('docker','docker-plain.svg'),0),("Azure",ic('azure','azure-plain.svg'),0),("Linux",ic('linux','linux-plain.svg'),0),("CI/CD",None,0)]),
 ("06","Quality & Runtime",[("Git",ic('git','git-plain.svg'),0),("SonarQube",ic('sonarqube','sonarqube-line.svg'),0),("Tomcat",ic('tomcat','tomcat-line.svg'),0),("IntelliJ IDEA",ic('intellij','intellij-plain.svg'),0)]),
]
glyph={"REST":"{ }","SOAP":"&lt;/&gt;","Hexagonal":"<svg width=34 height=36 viewBox='0 0 34 36'><polygon points='17,2 32,10.5 32,25.5 17,34 2,25.5 2,10.5' fill=none stroke=currentColor stroke-width=3.2 /><circle cx=17 cy=18 r=4 fill=currentColor /></svg>","MyBatis":"SQL","JSF":"jsf","CI/CD":"<svg width=40 height=36 viewBox='0 0 40 36'><path d='M6 18a12 12 0 0 1 21-8' fill=none stroke=currentColor stroke-width=3.2 stroke-linecap=round /><path d='M34 18a12 12 0 0 1-21 8' fill=none stroke=currentColor stroke-width=3.2 stroke-linecap=round /><path d='M27 3v8h-8' fill=none stroke=currentColor stroke-width=3.2 stroke-linecap=round stroke-linejoin=round /><path d='M13 33v-8h8' fill=none stroke=currentColor stroke-width=3.2 stroke-linecap=round stroke-linejoin=round /></svg>"}
cards=''
for num,title,items in cats:
    tiles=''
    for name,src,prim in items:
        col='#22d3ee' if prim else '#cbd5e1'
        if src: icon=f'<div class="ico" style="{"width:84px;-webkit-mask-size:84px;" if name=="Oracle" else ""}background:{col};-webkit-mask-image:url({src})"></div>'
        else: icon=f'<div class="gly" style="color:{col}">{glyph[name]}</div>'
        tiles+=f'<div class="t{" p" if prim else ""}">{icon}<div class="n">{name}</div></div>'
    cards+=f'<div class="card"><div class="k">{num} <span>/</span> {title}</div><div class="tiles">{tiles}</div></div>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:transparent}}
#c{{width:1100px;padding:32px 32px;box-sizing:border-box;border-radius:22px;background:linear-gradient(180deg,#0b1628,#080e1a);font-family:Inter,sans-serif;position:relative}}
.h{{font-family:'DejaVu Sans Mono',monospace;color:#22d3ee;font-size:16px;letter-spacing:.06em;margin-bottom:22px}}
.h b{{color:#e2e8f0;font-family:Inter;font-size:26px;letter-spacing:-.01em;font-weight:600;display:block;margin-top:8px}}
.g{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.card{{border:1px solid #1e293b;background:rgba(15,23,42,.6);border-radius:16px;padding:18px 18px 16px}}
.k{{font-family:'DejaVu Sans Mono',monospace;font-size:15px;color:#94a3b8;margin-bottom:18px}} .k span{{color:#334155}}
.tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}
.t{{display:flex;flex-direction:column;align-items:center;gap:10px;padding:16px 4px 12px;border-radius:12px;background:#0f1a2e;border:1px solid #1a2740}}
.t.p{{border-color:rgba(34,211,238,.35);background:rgba(34,211,238,.06)}}
.ico{{width:40px;height:40px;-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}}
.gly{{height:40px;line-height:40px;display:flex;align-items:center;font-family:'DejaVu Sans Mono',monospace;font-size:24px;font-weight:bold}}
.n{{font-size:15px;color:#cbd5e1;font-weight:500;white-space:nowrap}}
.legend{{position:absolute;right:32px;top:40px;font-family:'DejaVu Sans Mono',monospace;font-size:14px;color:#8a99ae}}
.legend i{{display:inline-block;width:10px;height:10px;border-radius:3px;background:rgba(34,211,238,.5);margin-right:8px;vertical-align:-1px}}
</style></head><body><div id="c"><div class="h">// toolbox<b>Technology stack</b></div><div class="legend"><i></i>primary specialization</div><div class="g">{cards}</div></div></body></html>'''
open('/home/claude/build/stack.html','w').write(html)
