# web/templates/base.py - Template base con navigazione
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_base_template(page_title, page_content, active_page="home"):
    """
    Template base con navbar per navigazione multi-page

    Args:
        page_title: Titolo della pagina
        page_content: HTML del contenuto specifico
        active_page: Pagina attiva (per highlight navbar)
    """

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
      padding-bottom: 80px;
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

    /* NAVBAR */
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

    /* CONTENT AREA */
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

    /* LOADING INDICATOR */
    .loading {{
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: none;
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

  <!-- NAVBAR -->
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
    // Init Telegram WebApp
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();

    // Navigation handling con animazioni
    document.querySelectorAll('.nav-item').forEach(item => {{
      item.addEventListener('click', function(e) {{
        e.preventDefault();
        const href = this.getAttribute('href');

        // Haptic feedback
        Telegram.WebApp.HapticFeedback.impactOccurred('light');

        // Mostra loading
        document.getElementById('loading').classList.add('active');

        // Naviga dopo animazione
        setTimeout(() => {{
          window.location.href = href;
        }}, 200);
      }});
    }});

    // Smooth scroll to top on page load
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  </script>
</body>
</html>
"""