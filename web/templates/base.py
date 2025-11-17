# web/templates/base.py - Versione DEFINITIVA: LUSSO MINIMAL NERO/ORО, tutto centrato e pulito
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    sub_nav_html = ""
    if sub_nav:
        sub_nav_items = ""
        for item in sub_nav:
            active_class = "active" if item.get('active', False) else ""
            sub_nav_items += f'''
            <a href="{item['url']}" class="sub-nav-item {active_class}">
                <span class="sub-nav-icon">{item.get('icon', '')}</span>
                <span class="sub-nav-label">{item['label']}</span>
            </a>
            '''
        sub_nav_html = f'''
        <div class="sub-navbar">
            <div class="sub-nav-scroll">
                {sub_nav_items}
            </div>
        </div>
        '''

    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>{page_title}</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #000000;
      --surface: #0d0d0d;
      --gold: #d4af37;
      --gold-glow: rgba(212,175,55,0.3);
      --text: #ffffff;
      --text-dim: rgba(255,255,255,0.65);
    }}

    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ font-family: 'Inter', sans-serif; background:var(--bg); color:var(--text); min-height:100vh; overflow-x:hidden; }}

    /* SFONDO LUSSO */
    .bg-gradient {{
      position:fixed; inset:0; z-index:-2;
      background: radial-gradient(circle at 20% 80%, rgba(212,175,55,0.12) 0%, transparent 50%),
                  radial-gradient(circle at 80% 20%, rgba(212,175,55,0.08) 0%, transparent 50%);
    }}

    /* HEADER FISSO CON TITOLO CENTRATO + HAMBURGER E CHIUSURA */
    .header {{
      position:fixed; top:0; left:0; right:0; height:70px;
      background: rgba(0,0,0,0.7); backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(212,175,55,0.15);
      display:flex; align-items:center; justify-content:space-between;
      padding:0 20px; z-index:1002;
    }}
    .header-title {{
      position:absolute; left:50%; transform:translateX(-50%);
      font-size:18px; font-weight:700; letter-spacing:0.5px;
      background: linear-gradient(90deg, #d4af37, #fff);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    /* HAMBURGER ORO */
    .hamburger {{
      width:48px; height:48px; background:rgba(212,175,55,0.12);
      border:1px solid rgba(212,175,55,0.3); border-radius:16px;
      display:flex; align-items:center; justify-content:center;
      cursor:pointer; transition:all 0.3s;
    }}
    .hamburger:hover {{ background:rgba(212,175,55,0.2); }}
    .hamburger span,.hamburger span::before,.hamburger span::after {{
      width:20px; height:2px; background:var(--gold); border-radius:2px; transition:all 0.3s;
    }}
    .hamburger span::before{{content:'';position:absolute;top:-6px;}}
    .hamburger span::after{{content:'';position:absolute;top:6px;}}
    .hamburger.active span{{background:transparent;}}
    .hamburger.active span::before{{transform:rotate(45deg) translate(5px,5px);}}
    .hamburger.active span::after{{transform:rotate(-45deg) translate(5px,-5px);}}

    /* CHIUSURA X CENTRATA */
    .close-btn {{
      width:48px; height:48px; background:rgba(212,175,55,0.12);
      border:1px solid rgba(212,175,55,0.3); border-radius:16px;
      display:none; align-items:center; justify-content:center;
      cursor:pointer; transition:all 0.3s;
    }}
    .close-btn.active {{ display:flex; }}
    .close-btn:hover {{ background:rgba(212,175,55,0.2); }}

    /* DRAWER MINIMAL PREMIUM */
    .drawer {{
      position:fixed; top:0; left:-320px; width:320px; height:100vh;
      background: var(--surface);
      border-right:1px solid rgba(212,175,55,0.2);
      padding-top:90px; z-index:1001;
      transition:left 0.45s cubic-bezier(0.22,1,0.36,1);
      box-shadow: 15px 0 50px rgba(0,0,0,0.9);
    }}
    .drawer.open {{ left:0; }}

    .drawer-item {{
      display:flex; align-items:center; gap:20px;
      padding:20px 32px; color:var(--text-dim);
      text-decoration:none; font-weight:500; font-size:17px;
      transition:all 0.3s; position:relative;
    }}
    .drawer-item:hover {{
      background:rgba(212,175,55,0.08); color:white;
      padding-left:40px;
    }}
    .drawer-item.active {{
      color:var(--gold); font-weight:700;
      background:rgba(212,175,55,0.12);
    }}
    .drawer-item.active::before {{
      content:''; position:absolute; left:0; top:0; bottom:0;
      width:4px; background:var(--gold);
    }}

    /* OVERLAY */
    .drawer-overlay {{
      position:fixed; inset:0; background:rgba(0,0,0,0.85);
      opacity:0; visibility:hidden; transition:all 0.4s; z-index:1000;
    }}
    .drawer-overlay.active {{ opacity:1; visibility:visible; }}

    /* CONTENUTO CENTRATO */
    .content {{
      max-width:480px; margin:90px auto 40px; padding:0 24px;
    }}

    /* SUB-NAVBAR (se serve) */
    .sub-navbar {{ position:fixed; bottom:70px; left:0; right:0; background:rgba(13,13,13,0.95); backdrop-filter:blur(20px);
      border-top:1px solid rgba(212,175,55,0.15); padding:10px 0; z-index:999; }}
    .sub-nav-item.active {{ background:linear-gradient(135deg,var(--gold),#b8972e); color:black; }}

    /* LOADING */
    .loading {{ position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
      display:none; z-index:10000; }}
    .loading.active {{ display:block; }}
    .spinner {{ width:56px; height:56px; border:3px solid rgba(212,175,55,0.2);
      border-top-color:var(--gold); border-radius:50%; animation:spin 1s linear infinite; }}
    @keyframes spin {{ to {{ transform:rotate(360deg); }} }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>

  <!-- HEADER CON TITOLO CENTRATO -->
  <div class="header">
    <div class="hamburger" id="hamburger"><span></span></div>
    <div class="header-title">{page_title}</div>
    <div class="close-btn" id="closeBtn"><span style="font-size:24px;color:var(--gold);">×</span></div>
  </div>

  <!-- DRAWER LUSSO MINIMAL -->
  <div class="drawer" id="drawer">
    <a href="/" class="drawer-item {'active' if active_page == 'home' else ''}">
      <span>Home</span>
      <span>Home</span>
    </a>
    <a href="/menu" class="drawer-item {'active' if active_page == 'menu' else ''}">
      <span>Menu</span>
      <span>Menu</span>
    </a>
    <a href="/agent" class="drawer-item {'active' if active_page == 'agent' else ''}">
      <span>Agente</span>
      <span>Agente</span>
    </a>
    <a href="/finance" class="drawer-item {'active' if active_page == 'finance' else ''}">
      <span>Finanza</span>
      <span>Finanza</span>
    </a>
    <a href="/psychology" class="drawer-item {'active' if active_page == 'psychology' else ''}">
      <span>Supporto</span>
      <span>Supporto</span>
    </a>
  </div>
  <div class="drawer-overlay" id="overlay"></div>

  <div class="content" id="pageContent">
    {page_content}
  </div>

  {sub_nav_html}

  <div class="loading" id="loading"><div class="spinner"></div></div>

  <script>
    Telegram.WebApp.ready(); Telegram.WebApp.expand();

    const h = document.getElementById('hamburger');
    const c = document.getElementById('closeBtn');
    const d = document.getElementById('drawer');
    const o = document.getElementById('overlay');

    function openDrawer() {{
      d.classList.add('open'); o.classList.add('active');
      h.style.display='none'; c.classList.add('active');
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}
    function closeDrawer() {{
      d.classList.remove('open'); o.classList.remove('active');
      h.style.display='flex'; c.classList.remove('active');
    }}

    h.addEventListener('click', openDrawer);
    c.addEventListener('click', closeDrawer);
    o.addEventListener('click', closeDrawer);

    document.querySelectorAll('.drawer-item, .sub-nav-item').forEach(el => {{
      el.addEventListener('click', function(e) {{
        e.preventDefault();
        Telegram.WebApp.HapticFeedback.impactOccurred('light');
        document.getElementById('loading').classList.add('active');
        setTimeout(() => location.href = this.href, 300);
      }});
    }});
  </script>
</body>
</html>
"""