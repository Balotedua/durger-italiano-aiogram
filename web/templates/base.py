# web/templates/base.py - Template base con drawer laterale sinistro (sostituisce la navbar inferiore)
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    """
    Template base con drawer laterale sinistro invece della navbar inferiore

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva nel drawer
        sub_nav: Lista di dict per sub-navbar (rimasta invariata)
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
      padding-bottom: {'140px' if sub_nav else '20px'};
      position: relative;
      overflow-x: hidden;
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
      padding-left: 70px; /* spazio per il drawer chiuso */
      transition: padding-left 0.3s ease;
      animation: fadeIn 0.5s ease;
    }}

    .content.drawer-open {{
      padding-left: 280px;
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

    /* HAMBURGER BUTTON */
    .hamburger {{
      position: fixed;
      top: 20px;
      left: 20px;
      width: 44px;
      height: 44px;
      background: rgba(255,255,255,0.1);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1001;
      transition: all 0.3s ease;
    }}

    .hamburger:active {{
      transform: scale(0.9);
    }}

    .hamburger span {{
      width: 20px;
      height: 2px;
      background: white;
      border-radius: 1px;
      position: relative;
    }}

    .hamburger span::before,
    .hamburger span::after {{
      content: '';
      position: absolute;
      width: 20px;
      height: 2px;
      background: white;
      border-radius: 1px;
      transition: all 0.3s ease;
    }}

    .hamburger span::before {{ top: -6px; }}
    .hamburger span::after {{ top: 6px; }}

    .hamburger.active span {{ background: transparent; }}
    .hamburger.active span::before {{ transform: translateY(6px) rotate(45deg); }}
    .hamburger.active span::after {{ transform: translateY(-6px) rotate(-45deg); }}

    /* DRAWER LATERALE SINISTRO */
    .drawer {{
      position: fixed;
      top: 0;
      left: -280px;
      width: 280px;
      height: 100vh;
      background: rgba(10,10,20,0.98);
      backdrop-filter: blur(20px);
      border-right: 1px solid rgba(255,255,255,0.1);
      padding-top: 80px;
      transition: left 0.3s ease;
      z-index: 1000;
      overflow-y: auto;
    }}

    .drawer.open {{
      left: 0;
    }}

    .drawer-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.7);
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s ease;
      z-index: 999;
    }}

    .drawer-overlay.active {{
      opacity: 1;
      visibility: visible;
    }}

    .drawer-item {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 16px 24px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 16px;
      font-weight: 600;
      transition: all 0.3s ease;
    }}

    .drawer-item:hover {{
      background: rgba(255,255,255,0.08);
      color: white;
    }}

    .drawer-item.active {{
      background: linear-gradient(90deg, var(--primary), transparent);
      color: white;
      border-left: 4px solid var(--accent);
    }}

    .drawer-icon {{
      font-size: 24px;
    }}

    /* SUB NAVBAR (rimasta identica) */
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

    .sub-nav-scroll::-webkit-scrollbar {{ display: none; }}

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

    .sub-nav-item:active {{ transform: scale(0.95); }}
    .sub-nav-item.active {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-color: transparent;
      color: white;
    }}

    .sub-nav-icon {{ font-size: 18px; }}

    /* LOADING */
    .loading {{
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: none;
      z-index: 10000;
    }}

    .loading.active {{ display: block; }}

    .spinner {{
      width: 50px;
      height: 50px;
      border: 4px solid rgba(255,255,255,0.1);
      border-top-color: var(--primary);
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}

    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>

  <!-- HAMBURGER -->
  <div class="hamburger" id="hamburger">
    <span></span>
  </div>

  <!-- DRAWER LATERALE -->
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

  <!-- OVERLAY -->
  <div class="drawer-overlay" id="overlay"></div>

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

    const hamburger = document.getElementById('hamburger');
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('overlay');
    const content = document.getElementById('pageContent');

    function toggleDrawer() {{
      hamburger.classList.toggle('active');
      drawer.classList.toggle('open');
      overlay.classList.toggle('active');
      content.classList.toggle('drawer-open');
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    hamburger.addEventListener('click', toggleDrawer);
    overlay.addEventListener('click', () => {{
      if (drawer.classList.contains('open')) toggleDrawer();
    }});

    // Navigazione con loading
    document.querySelectorAll('.drawer-item, .sub-nav-item').forEach(item => {{
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