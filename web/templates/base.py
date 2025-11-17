# web/templates/base.py - Versione LUSSO: drawer sinistro nero/oro, contenuto perfettamente centrato
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    # Sub-navbar invariata
    sub_nav_html = ""
    if sub_nav:
        sub_nav_items = ""
        for item in sub_nav:
            active_class = "active" if item.get('active', False) else ""
            sub_nav_items += f'''
            <a href="{item['url']}" class="sub-nav-item {active_class}">
                <span class="sub-nav-icon">{item['icon']}</span>
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
  < title>{page_title}</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #0f0f1a;
      --card: #1a1a2e;
      --gold: #ffd700;
      --gold-light: #f9c74f;
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.6);
    }}

    * {{ margin:0; padding:0; box-sizing:border-box; }}

    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding-bottom: {'140px' if sub_nav else '40px'};
      overflow-x: hidden;
    }}

    /* SFONDO GRADIENT LUSSO */
    .bg-gradient {{
      position: fixed;
      inset: 0;
      z-index: -1;
      background: radial-gradient(circle at top left, rgba(255,215,0,0.15), transparent 50%),
                  radial-gradient(circle at bottom right, rgba(255,215,0,0.1), transparent 60%);
      background-size: 200% 200%;
      animation: luxuryGlow 20s ease infinite;
    }}
    @keyframes luxuryGlow {{ 0%,100% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} }}

    /* CONTENUTO SEMPRE CENTRATO */
    .content {{
      max-width: 480px;
      margin: 0 auto;
      padding: 20px 20px;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* HAMBURGER ORO */
    .hamburger {{
      position: fixed;
      top: 20px;
      left: 20px;
      width: 48px; height: 48px;
      background: rgba(255,215,0,0.15);
      border: 1.5px solid var(--gold);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1001;
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }}
    .hamburger:hover {{ background: rgba(255,215,0,0.25); transform: scale(1.05); }}
    .hamburger span, .hamburger span::before, .hamburger span::after {{
      width: 22px; height: 2px;
      background: var(--gold);
      border-radius: 2px;
      transition: all 0.3s ease;
    }}
    .hamburger span::before {{ content:''; position:absolute; top:-7px; }}
    .hamburger span::after {{ content:''; position:absolute; top:7px; }}
    .hamburger.active span {{ background:transparent; }}
    .hamburger.active span::before {{ transform: translateY(7px) rotate(45deg); }}
    .hamburger.active span::after {{ transform: translateY(-7px) rotate(-45deg); }}

    /* DRAWER LUSSO NERO/ORo */
    .drawer {{
      position: fixed;
      top: 0; left: -300px;
      width: 300px;
      height: 100vh;
      background: linear-gradient(135deg, #0f0f1a 0%, #16213e 100%);
      border-right: 1px solid rgba(255,215,0,0.3);
      padding-top: 90px;
      transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 1000;
      box-shadow: 10px 0 40px rgba(0,0,0,0.8);
    }}
    .drawer.open {{ left: 0; }}

    .drawer::before {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 200px;
      background: linear-gradient(to bottom, rgba(255,215,0,0.08), transparent);
      pointer-events: none;
    }}

    .drawer-item {{
      display: flex;
      align-items: center;
      gap: 18px;
      padding: 18px 28px;
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 500;
      font-size: 16px;
      transition: all 0.3s ease;
      position: relative;
    }}
    .drawer-item:hover {{
      background: rgba(255,215,0,0.1);
      color: white;
      padding-left: 36px;
    }}
    .drawer-item.active {{
      color: var(--gold);
      background: rgba(255,215,0,0.15);
      font-weight: 700;
    }}
    .drawer-item.active::before {{
      content: '';
      position: absolute;
      left: 0;
      top: 0; bottom: 0;
      width: 4px;
      background: var(--gold);
    }}
    .drawer-icon {{ font-size: 26px; }}

    /* OVERLAY */
    .drawer-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      opacity: 0;
      visibility: hidden;
      transition: all 0.4s ease;
      z-index: 999;
    }}
    .drawer-overlay.active {{ opacity: 1; visibility: visible; }}

    /* SUB-NAVBAR invariata (se presente) */
    .sub-navbar {{ position: fixed; bottom: 70px; left: 0; right: 0; background: rgba(15,15,25,0.95); backdrop-filter: blur(20px); border-top: 1px solid rgba(255,255,255,0.08); padding: 8px 0; z-index: 999; }}
    .sub-nav-scroll {{ display: flex; gap: 8px; padding: 0 12px; overflow-x: auto; scrollbar-width: none; }}
    .sub-nav-scroll::-webkit-scrollbar {{ display: none; }}
    .sub-nav-item {{ flex-shrink: 0; display: flex; align-items: center; gap: 8px; padding: 10px 16px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; color: var(--text-muted); font-size: 14px; font-weight: 600; text-decoration: none; transition: all 0.3s; }}
    .sub-nav-item:active {{ transform: scale(0.95); }}
    .sub-nav-item.active {{ background: linear-gradient(135deg, #ffd700, #f9c74f); color: #000; }}

    /* LOADING */
    .loading {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%); display: none; z-index: 10000; }}
    .loading.active {{ display: block; }}
    .spinner {{ width: 50px; height: 50px; border: 4px solid rgba(255,215,0,0.2); border-top-color: var(--gold); border-radius: 50%; animation: spin 1s linear infinite; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>

  <!-- HAMBURGER ORO -->
  <div class="hamburger" id="hamburger"><span></span></div>

  <!-- DRAWER LUSSO -->
  <div class="drawer" id="drawer">
    <a href="/" class="drawer-item {'active' if active_page == 'home' else ''}">
      <span class="drawer-icon">Home</span>
      <span>Home</span>
    </a>
    <a href="/menu" class="drawer-item {'active' if active_page == 'menu' else ''}">
      <span class="drawer-icon">Menu</span>
      <span>Menu</span>
    </a>
    <a href="/agent" class="drawer-item {'active' if active_page == 'agent' else ''}">
      <span class="drawer-icon">Agente</span>
      <span>Agente</span>
    </a>
    <a href="/finance" class="drawer-item {'active' if active_page == 'finance' else ''}">
      <span class="drawer-icon">Finanza</span>
      <span>Finanza</span>
    </a>
    <a href="/psychology" class="drawer-item {'active' if active_page == 'psychology' else ''}">
      <span class="drawer-icon">Supporto</span>
      <span>Supporto</span>
    </a>
  </div>

  <div class="drawer-overlay" id="overlay"></div>

  <!-- CONTENUTO CENTRATO -->
  <div class="content" id="pageContent">
    {page_content}
  </div>

  {sub_nav_html}

  <div class="loading" id="loading"><div class="spinner"></div></div>

  <script>
    Telegram.WebApp.ready(); Telegram.WebApp.expand();

    const h = document.getElementById('hamburger');
    const d = document.getElementById('drawer');
    const o = document.getElementById('overlay');

    function toggle() {{
      h.classList.toggle('active');
      d.classList.toggle('open');
      o.classList.toggle('active');
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    h.addEventListener('click', toggle);
    o.addEventListener('click', () => {{ if(d.classList.contains('open')) toggle(); }});

    document.querySelectorAll('.drawer-item, .sub-nav-item').forEach(el => {{
      el.addEventListener('click', function(e) {{
        e.preventDefault();
        Telegram.WebApp.HapticFeedback.impactOccurred('light');
        document.getElementById('loading').classList.add('active');
        setTimeout(() => location.href = this.getAttribute('href'), 250);
      }});
    }});
  </script>
</body>
</html>
"""