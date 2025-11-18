# web/templates/base.py - Menu a tendina COMPLETO
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    """
    Template base con menu a tendina lussuoso nero/oro - COMPLETO

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva nel menu
        sub_nav: Lista dict per sub-navbar
    """

    # Sub-navbar
    sub_nav_html = ""
    if sub_nav:
        sub_nav_items = "".join([
            f'''<a href="{item['url']}" class="sub-nav-item {'active' if item.get('active') else ''}">
                <span class="sub-nav-icon">{item.get('icon', '')}</span>
                <span class="sub-nav-label">{item['label']}</span>
            </a>'''
            for item in sub_nav
        ])
        sub_nav_html = f'<div class="sub-navbar"><div class="sub-nav-scroll">{sub_nav_items}</div></div>'

    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #000000;
      --surface: #0d0d0d;
      --gold: #d4af37;
      --gold-light: #f4e4a0;
      --text: #ffffff;
      --text-dim: rgba(255,255,255,0.65);
    }}

    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ 
      font-family: 'Inter', sans-serif; 
      background:var(--bg); 
      color:var(--text); 
      min-height:100vh;
      padding-bottom: {'90px' if sub_nav else '20px'};
    }}

    .bg-gradient {{
      position:fixed; inset:0; z-index:-2;
      background: radial-gradient(circle at 20% 80%, rgba(212,175,55,0.12), transparent 50%),
                  radial-gradient(circle at 80% 20%, rgba(212,175,55,0.08), transparent 50%);
    }}

    /* HAMBURGER */
    .menu-toggle {{
      position: fixed; top: 20px; left: 20px;
      width: 56px; height: 56px;
      background: rgba(212,175,55,0.15);
      border: 1px solid rgba(212,175,55,0.4);
      border-radius: 16px;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.22,1,0.36,1);
      z-index: 1002;
      backdrop-filter: blur(10px);
    }}

    .menu-toggle:hover {{
      background: rgba(212,175,55,0.25);
      transform: scale(1.05);
    }}

    .menu-toggle span {{
      width: 24px; height: 2px;
      background: var(--gold);
      border-radius: 2px;
      position: relative;
      transition: all 0.3s;
    }}

    .menu-toggle span::before,
    .menu-toggle span::after {{
      content: ''; position: absolute;
      width: 24px; height: 2px;
      background: var(--gold);
      border-radius: 2px;
      transition: all 0.3s;
    }}

    .menu-toggle span::before {{ top: -8px; }}
    .menu-toggle span::after {{ top: 8px; }}

    .menu-toggle.active span {{ background: transparent; }}
    .menu-toggle.active span::before {{
      transform: rotate(45deg) translate(5px, 5px);
    }}
    .menu-toggle.active span::after {{
      transform: rotate(-45deg) translate(5px, -5px);
    }}

    /* DRAWER */
    .drawer {{
      position: fixed; top: 0; left: -340px;
      width: 320px; height: 100vh;
      background: var(--surface);
      border-right: 1px solid rgba(212,175,55,0.3);
      padding: 100px 0 40px 0;
      z-index: 1001;
      transition: left 0.5s cubic-bezier(0.22,1,0.36,1);
      overflow-y: auto;
      box-shadow: 20px 0 60px rgba(0,0,0,0.8);
    }}

    .drawer.open {{ left: 0; }}

    .drawer-section {{
      padding: 20px 0;
      border-bottom: 1px solid rgba(212,175,55,0.1);
    }}

    .drawer-section-title {{
      padding: 0 32px 12px;
      font-size: 11px;
      font-weight: 700;
      color: rgba(212,175,55,0.6);
      text-transform: uppercase;
      letter-spacing: 2px;
    }}

    .drawer-item {{
      display: flex; align-items: center; gap: 16px;
      padding: 18px 32px;
      color: var(--text-dim);
      text-decoration: none;
      font-weight: 600; font-size: 16px;
      transition: all 0.3s ease;
      position: relative;
      border-left: 4px solid transparent;
    }}

    .drawer-item:hover {{
      background: rgba(212,175,55,0.1);
      color: var(--gold-light);
      padding-left: 36px;
      border-left-color: var(--gold);
    }}

    .drawer-item.active {{
      background: rgba(212,175,55,0.15);
      color: var(--gold);
      border-left-color: var(--gold);
      font-weight: 700;
    }}

    .drawer-icon {{ font-size: 22px; width: 24px; text-align: center; }}

    /* OVERLAY */
    .drawer-overlay {{
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.8);
      opacity: 0; visibility: hidden;
      transition: all 0.4s ease;
      z-index: 1000;
      backdrop-filter: blur(5px);
    }}

    .drawer-overlay.active {{ opacity: 1; visibility: visible; }}

    /* CONTENT */
    .content {{
      max-width: 480px;
      margin: 0 auto;
      padding: 40px 24px;
      animation: fadeIn 0.6s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* SUB-NAVBAR */
    .sub-navbar {{
      position: fixed; bottom: 0; left: 0; right: 0;
      background: rgba(13,13,13,0.95);
      backdrop-filter: blur(20px);
      border-top: 1px solid rgba(212,175,55,0.2);
      padding: 12px 16px;
      z-index: 999;
    }}

    .sub-nav-scroll {{
      display: flex; gap: 8px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}

    .sub-nav-scroll::-webkit-scrollbar {{ display: none; }}

    .sub-nav-item {{
      flex-shrink: 0;
      display: flex; align-items: center; gap: 8px;
      padding: 12px 18px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(212,175,55,0.2);
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--text-dim);
      font-size: 14px; font-weight: 600;
      white-space: nowrap;
    }}

    .sub-nav-item:hover {{
      background: rgba(212,175,55,0.1);
      color: var(--gold-light);
    }}

    .sub-nav-item.active {{
      background: linear-gradient(135deg, var(--gold), #b8972e);
      border-color: transparent;
      color: black;
      font-weight: 700;
    }}

    .sub-nav-icon {{ font-size: 16px; }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>

  <div class="menu-toggle" id="menuToggle"><span></span></div>

  <div class="drawer" id="drawer">
    <!-- PRINCIPALE -->
    <div class="drawer-section">
      <div class="drawer-section-title">Principale</div>
      <a href="/" class="drawer-item {'active' if active_page == 'home' else ''}">
        <span class="drawer-icon">🏠</span><span>Home</span>
      </a>
      <a href="/recap" class="drawer-item {'active' if active_page == 'recap' else ''}">
        <span class="drawer-icon">📊</span><span>Dashboard Recap</span>
      </a>
    </div>

    <!-- LAVORO & PRODUTTIVITÀ -->
    <div class="drawer-section">
      <div class="drawer-section-title">Lavoro & Produttività</div>
      <a href="/career" class="drawer-item {'active' if active_page == 'career' else ''}">
        <span class="drawer-icon">🎖️</span><span>Badge & Career</span>
      </a>
      <a href="/time" class="drawer-item {'active' if active_page == 'time' else ''}">
        <span class="drawer-icon">⏰</span><span>Gestione Tempo</span>
      </a>
      <a href="/notes" class="drawer-item {'active' if active_page == 'notes' else ''}">
        <span class="drawer-icon">📝</span><span>Note</span>
      </a>
    </div>

    <!-- BENESSERE -->
    <div class="drawer-section">
      <div class="drawer-section-title">Benessere</div>
      <a href="/mental" class="drawer-item {'active' if active_page == 'mental' else ''}">
        <span class="drawer-icon">🧠</span><span>Salute Mentale</span>
      </a>
      <a href="/fitness" class="drawer-item {'active' if active_page == 'fitness' else ''}">
        <span class="drawer-icon">💪</span><span>Fitness</span>
      </a>
      <a href="/detox" class="drawer-item {'active' if active_page == 'detox' else ''}">
        <span class="drawer-icon">🌿</span><span>Detox Digitale</span>
      </a>
    </div>

    <!-- FINANZA & ALTRO -->
    <div class="drawer-section">
      <div class="drawer-section-title">Finanza & Extra</div>
      <a href="/finance" class="drawer-item {'active' if active_page == 'finance' else ''}">
        <span class="drawer-icon">💰</span><span>Finanza</span>
      </a>
      <a href="/jolly" class="drawer-item {'active' if active_page == 'jolly' else ''}">
        <span class="drawer-icon">🃏</span><span>Jolly</span>
      </a>
    </div>

    <!-- SERVIZI -->
    <div class="drawer-section">
      <div class="drawer-section-title">Servizi</div>
      <a href="/news" class="drawer-item {'active' if active_page == 'news' else ''}">
        <span class="drawer-icon">📰</span><span>News & Skills</span>
      </a>
      <a href="/menu" class="drawer-item {'active' if active_page == 'menu' else ''}">
        <span class="drawer-icon">🍕</span><span>Menu</span>
      </a>
      <a href="/agent" class="drawer-item {'active' if active_page == 'agent' else ''}">
        <span class="drawer-icon">🤖</span><span>AI Agent</span>
      </a>
    </div>
  </div>

  <div class="drawer-overlay" id="overlay"></div>

  <div class="content">{page_content}</div>

  {sub_nav_html}

  <script>
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();

    const toggle = document.getElementById('menuToggle');
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('overlay');

    toggle.onclick = () => {{
      const open = drawer.classList.toggle('open');
      overlay.classList.toggle('active', open);
      toggle.classList.toggle('active', open);
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }};

    overlay.onclick = () => {{
      drawer.classList.remove('open');
      overlay.classList.remove('active');
      toggle.classList.remove('active');
    }};

    document.querySelectorAll('.drawer-item, .sub-nav-item').forEach(item => {{
      item.onclick = (e) => {{
        e.preventDefault();
        Telegram.WebApp.HapticFeedback.impactOccurred('light');
        setTimeout(() => window.location.href = item.href, 200);
      }};
    }});
  </script>
</body>
</html>"""


import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    """
    Template base con navbar principale e opzionale sub-navbar

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva nella navbar principale
        sub_nav: Lista di dict per sub-navbar es: [{'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': True}]
    """

    # Sub-navbar HTML (se presente)
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
  <title>{page_title}</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #6366f1;
      --secondary: #8b5cf6;
      --accent: #ec4899;
      --success: #10b981;
      --bg: #0a0a0f;
      --card: rgba(255,255,255,0.08);
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.7);
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding-bottom: {'140px' if sub_nav else '80px'};
      position: relative;
    }}

    /* BACKGROUND */
    .bg-gradient {{
      position: fixed;
      inset: 0;
      z-index: -1;
      background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
      background-size: 400% 400%;
      animation: gradientShift 15s ease infinite;
      opacity: 0.3;
    }}

    @keyframes gradientShift {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    /* CONTENT */
    .content {{
      padding: 20px 16px;
      animation: fadeIn 0.5s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* PAGE HEADER */
    .page-header {{
      text-align: center;
      margin-bottom: 32px;
    }}

    .page-header h1 {{
      font-size: 32px;
      font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}

    .page-header p {{
      color: var(--text-muted);
      font-size: 14px;
    }}

    /* SUB NAVBAR (sopra navbar principale) */
    .sub-navbar {{
      position: fixed;
      bottom: 70px;
      left: 0;
      right: 0;
      background: rgba(15,15,25,0.95);
      backdrop-filter: blur(20px);
      border-top: 1px solid rgba(255,255,255,0.08);
      padding: 8px 0;
      z-index: 999;
      box-shadow: 0 -2px 20px rgba(0,0,0,0.2);
    }}

    .sub-nav-scroll {{
      display: flex;
      gap: 8px;
      padding: 0 12px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}

    .sub-nav-scroll::-webkit-scrollbar {{
      display: none;
    }}

    .sub-nav-item {{
      flex-shrink: 0;
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px 16px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--text-muted);
      font-size: 14px;
      font-weight: 600;
      white-space: nowrap;
    }}

    .sub-nav-item:active {{
      transform: scale(0.95);
    }}

    .sub-nav-item.active {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-color: transparent;
      color: white;
    }}

    .sub-nav-icon {{
      font-size: 18px;
    }}

    /* MAIN NAVBAR */
    .navbar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(10,10,15,0.95);
      backdrop-filter: blur(20px);
      border-top: 1px solid rgba(255,255,255,0.1);
      padding: 12px 8px;
      display: flex;
      justify-content: space-around;
      z-index: 1000;
      box-shadow: 0 -4px 20px rgba(0,0,0,0.3);
    }}

    .nav-item {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      padding: 8px;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--text-muted);
    }}

    .nav-item:active {{
      transform: scale(0.95);
    }}

    .nav-item.active {{
      background: rgba(99,102,241,0.2);
      color: var(--primary);
    }}

    .nav-icon {{
      font-size: 24px;
    }}

    .nav-label {{
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* LOADING */
    .loading {{
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: none;
      z-index: 10000;
    }}

    .loading.active {{
      display: block;
    }}

    .spinner {{
      width: 50px;
      height: 50px;
      border: 4px solid rgba(255,255,255,0.1);
      border-top-color: var(--primary);
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}

    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>

  <div class="content" id="pageContent">
    {page_content}
  </div>

  {sub_nav_html}

  <!-- MAIN NAVBAR -->
  <nav class="navbar">
    <a href="/" class="nav-item {'active' if active_page == 'home' else ''}">
      <div class="nav-icon">🏠</div>
      <div class="nav-label">Home</div>
    </a>
    <a href="/menu" class="nav-item {'active' if active_page == 'menu' else ''}">
      <div class="nav-icon">🍕</div>
      <div class="nav-label">Menu</div>
    </a>
    <a href="/agent" class="nav-item {'active' if active_page == 'agent' else ''}">
      <div class="nav-icon">🤖</div>
      <div class="nav-label">Agente</div>
    </a>
    <a href="/finance" class="nav-item {'active' if active_page == 'finance' else ''}">
      <div class="nav-icon">💰</div>
      <div class="nav-label">Finanza</div>
    </a>
    <a href="/psychology" class="nav-item {'active' if active_page == 'psychology' else ''}">
      <div class="nav-icon">🧠</div>
      <div class="nav-label">Supporto</div>
    </a>
  </nav>

  <!-- LOADING -->
  <div class="loading" id="loading">
    <div class="spinner"></div>
  </div>

  <script>
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();

    // Navigation con animazioni
    document.querySelectorAll('.nav-item, .sub-nav-item').forEach(item => {{
      item.addEventListener('click', function(e) {{
        e.preventDefault();
        const href = this.getAttribute('href');

        Telegram.WebApp.HapticFeedback.impactOccurred('light');
        document.getElementById('loading').classList.add('active');

        setTimeout(() => {{
          window.location.href = href;
        }}, 200);
      }});
    }});

    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  </script>
</body>
</html>
"""