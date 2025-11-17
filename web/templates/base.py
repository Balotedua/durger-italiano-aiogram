# web/templates/base.py - Template base con navigazione e sub-navigazione
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home", sub_nav=None):
    """
    Template base con sidebar e opzionale sub-navbar

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva nella sidebar
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

    /* SIDEBAR */
    .sidebar {{
      position: fixed;
      left: 0;
      top: 0;
      bottom: 0;
      width: 80px;
      background: rgba(10,10,15,0.95);
      backdrop-filter: blur(20px);
      border-right: 1px solid rgba(255,255,255,0.1);
      padding: 20px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 1000;
      box-shadow: 4px 0 20px rgba(0,0,0,0.3);
    }}

    .nav-item {{
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      padding: 16px 8px;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--text-muted);
      border-left: 3px solid transparent;
    }}

    .nav-item:active {{
      transform: scale(0.95);
    }}

    .nav-item.active {{
      background: rgba(99,102,241,0.2);
      color: var(--primary);
      border-left-color: var(--primary);
    }}

    .nav-icon {{
      font-size: 24px;
    }}

    .nav-label {{
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      text-align: center;
    }}

    /* CONTENT */
    .content {{
      margin-left: 80px;
      padding: 20px 16px;
      animation: fadeIn 0.5s ease;
      min-height: 100vh;
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

    /* SUB NAVBAR */
    .sub-navbar {{
      background: rgba(15,15,25,0.95);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      padding: 12px;
      margin: 20px 0;
      box-shadow: 0 2px 20px rgba(0,0,0,0.2);
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

  <!-- SIDEBAR -->
  <nav class="sidebar">
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