# web/templates/base.py - Template base con menù a tendina lussuoso
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    """
    Template base con menù a tendina lussuoso nero/oro

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva nel menù
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
      --gold-light: #f4e4a0;
      --gold-glow: rgba(212,175,55,0.3);
      --text: #ffffff;
      --text-dim: rgba(255,255,255,0.65);
    }}

    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ 
      font-family: 'Inter', sans-serif; 
      background:var(--bg); 
      color:var(--text); 
      min-height:100vh; 
      overflow-x:hidden;
    }}

    /* SFONDO LUSSO */
    .bg-gradient {{
      position:fixed; 
      inset:0; 
      z-index:-2;
      background: 
        radial-gradient(circle at 20% 80%, rgba(212,175,55,0.12) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(212,175,55,0.08) 0%, transparent 50%),
        linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
    }}

    /* HAMBURGER ORO FLOTTANTE */
    .menu-toggle {{
      position: fixed;
      top: 20px;
      left: 20px;
      width: 56px;
      height: 56px;
      background: rgba(212,175,55,0.15);
      border: 1px solid rgba(212,175,55,0.4);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.22,1,0.36,1);
      z-index: 1002;
      backdrop-filter: blur(10px);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}

    .menu-toggle:hover {{
      background: rgba(212,175,55,0.25);
      border-color: var(--gold);
      transform: scale(1.05);
    }}

    .menu-toggle span {{
      width: 24px;
      height: 2px;
      background: var(--gold);
      border-radius: 2px;
      position: relative;
      transition: all 0.3s;
    }}

    .menu-toggle span::before,
    .menu-toggle span::after {{
      content: '';
      position: absolute;
      width: 24px;
      height: 2px;
      background: var(--gold);
      border-radius: 2px;
      transition: all 0.3s;
    }}

    .menu-toggle span::before {{
      top: -8px;
    }}

    .menu-toggle span::after {{
      top: 8px;
    }}

    .menu-toggle.active {{
      background: rgba(212,175,55,0.25);
      border-color: var(--gold-light);
    }}

    .menu-toggle.active span {{
      background: transparent;
    }}

    .menu-toggle.active span::before {{
      transform: rotate(45deg) translate(5px, 5px);
      background: var(--gold-light);
    }}

    .menu-toggle.active span::after {{
      transform: rotate(-45deg) translate(5px, -5px);
      background: var(--gold-light);
    }}

    /* DRAWER LUSSO */
    .drawer {{
      position: fixed;
      top: 0;
      left: -320px;
      width: 300px;
      height: 100vh;
      background: var(--surface);
      border-right: 1px solid rgba(212,175,55,0.3);
      padding: 100px 0 40px 0;
      z-index: 1001;
      transition: left 0.5s cubic-bezier(0.22,1,0.36,1);
      box-shadow: 20px 0 60px rgba(0,0,0,0.8);
    }}

    .drawer.open {{
      left: 0;
    }}

    .drawer-item {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 18px 32px;
      color: var(--text-dim);
      text-decoration: none;
      font-weight: 600;
      font-size: 16px;
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

    .drawer-icon {{
      font-size: 22px;
      width: 24px;
      text-align: center;
    }}

    /* OVERLAY */
    .drawer-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      opacity: 0;
      visibility: hidden;
      transition: all 0.4s ease;
      z-index: 1000;
      backdrop-filter: blur(5px);
    }}

    .drawer-overlay.active {{
      opacity: 1;
      visibility: visible;
    }}

    /* CONTENUTO CENTRATO */
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
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(13,13,13,0.95);
      backdrop-filter: blur(20px);
      border-top: 1px solid rgba(212,175,55,0.2);
      padding: 12px 16px;
      z-index: 999;
    }}

    .sub-nav-scroll {{
      display: flex;
      gap: 8px;
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
      padding: 12px 18px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(212,175,55,0.2);
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--text-dim);
      font-size: 14px;
      font-weight: 600;
      white-space: nowrap;
    }}

    .sub-nav-item:hover {{
      background: rgba(212,175,55,0.1);
      border-color: var(--gold);
      color: var(--gold-light);
    }}

    .sub-nav-item.active {{
      background: linear-gradient(135deg, var(--gold), #b8972e);
      border-color: transparent;
      color: black;
      font-weight: 700;
    }}

    .sub-nav-icon {{
      font-size: 16px;
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
      width: 56px;
      height: 56px;
      border: 3px solid rgba(212,175,55,0.2);
      border-top-color: var(--gold);
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

  <!-- MENU TOGGLE -->
  <div class="menu-toggle" id="menuToggle">
    <span></span>
  </div>

  <!-- DRAWER LUSSO -->
  <div class="drawer" id="drawer">
    <a href="/" class="drawer-item {'active' if active_page == 'home' else ''}">
      <span class="drawer-icon">🏠</span>
      <span>Home</span>
    </a>
    <a href="/menu" class="drawer-item {'active' if active_page == 'menu' else ''}">
      <span class="drawer-icon">🍕</span>
      <span>Menu</span>
    </a>
    <a href="/agent" class="drawer-item {'active' if active_page == 'agent' else ''}">
      <span class="drawer-icon">🤖</span>
      <span>Agente</span>
    </a>
    <a href="/finance" class="drawer-item {'active' if active_page == 'finance' else ''}">
      <span class="drawer-icon">💰</span>
      <span>Finanza</span>
    </a>
    <a href="/psychology" class="drawer-item {'active' if active_page == 'psychology' else ''}">
      <span class="drawer-icon">🧠</span>
      <span>Supporto</span>
    </a>
  </div>

  <!-- OVERLAY -->
  <div class="drawer-overlay" id="overlay"></div>

  <!-- CONTENUTO PRINCIPALE -->
  <div class="content" id="pageContent">
    {page_content}
  </div>

  {sub_nav_html}

  <!-- LOADING -->
  <div class="loading" id="loading">
    <div class="spinner"></div>
  </div>

  <script>
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();

    const menuToggle = document.getElementById('menuToggle');
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('overlay');

    function toggleDrawer() {{
      const isOpen = drawer.classList.contains('open');

      if (isOpen) {{
        closeDrawer();
      }} else {{
        openDrawer();
      }}
    }}

    function openDrawer() {{
      drawer.classList.add('open');
      overlay.classList.add('active');
      menuToggle.classList.add('active');
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    function closeDrawer() {{
      drawer.classList.remove('open');
      overlay.classList.remove('active');
      menuToggle.classList.remove('active');
    }}

    menuToggle.addEventListener('click', toggleDrawer);
    overlay.addEventListener('click', closeDrawer);

    // Navigazione con loading
    document.querySelectorAll('.drawer-item, .sub-nav-item').forEach(item => {{
      item.addEventListener('click', function(e) {{
        e.preventDefault();
        const href = this.getAttribute('href');

        Telegram.WebApp.HapticFeedback.impactOccurred('light');
        document.getElementById('loading').classList.add('active');
        closeDrawer();

        setTimeout(() => {{
          window.location.href = href;
        }}, 400);
      }});
    }});

    // Chiudi drawer con ESC
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeDrawer();
    }});
  </script>
</body>
</html>"""