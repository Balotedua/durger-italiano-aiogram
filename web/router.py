# web/router.py - Router per navigazione multi-page
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiohttp import web
from web.templates.base import get_base_template
from web.templates.agent import generate_agent_page


def generate_home_page():
    """Homepage con link alle sezioni"""
    content = """
    <div class="page-header">
      <h1>🏠 Durger King</h1>
      <p>La tua app completa per tutto</p>
    </div>

    <style>
      .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        max-width: 600px;
        margin: 0 auto;
      }

      .feature-card {
        padding: 32px 24px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 24px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        color: inherit;
      }

      .feature-card:active {
        transform: scale(0.95);
        background: rgba(99,102,241,0.2);
      }

      .feature-icon {
        font-size: 48px;
        margin-bottom: 12px;
      }

      .feature-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
      }

      .feature-desc {
        font-size: 13px;
        color: var(--text-muted);
      }
    </style>

    <div class="feature-grid">
      <a href="/menu" class="feature-card">
        <div class="feature-icon">🍕</div>
        <div class="feature-title">Menu</div>
        <div class="feature-desc">Ordina cibo italiano</div>
      </a>

      <a href="/agent" class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Assistente</div>
        <div class="feature-desc">AI H24 per te</div>
      </a>

      <a href="/finance" class="feature-card">
        <div class="feature-icon">💰</div>
        <div class="feature-title">Finanza</div>
        <div class="feature-desc">Gestisci soldi</div>
      </a>

      <a href="/psychology" class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Supporto</div>
        <div class="feature-desc">Benessere mentale</div>
      </a>
    </div>
    """
    return get_base_template("Home", content, "home")


def generate_menu_page():
    """Pagina menu ristorante (il tuo codice esistente)"""
    # Importa il menu dal file menu.py
    try:
        from web.templates.menu import generate_menu_html
        return generate_menu_html()
    except ImportError:
        # Fallback se il file non esiste
        return get_base_template("Menu", "<p>Menu non disponibile</p>", "menu")


def generate_finance_page():
    """Pagina finanza"""
    content = """
    <div class="page-header">
      <h1>💰 Finanza Personale</h1>
      <p>Gestisci il tuo budget</p>
    </div>

    <style>
      .balance-card {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        padding: 32px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 20px 60px rgba(99,102,241,0.4);
      }

      .balance-label {
        font-size: 14px;
        opacity: 0.9;
        margin-bottom: 8px;
      }

      .balance-amount {
        font-size: 48px;
        font-weight: 900;
      }

      .transactions {
        display: flex;
        flex-direction: column;
        gap: 12px;
      }

      .transaction {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background: rgba(255,255,255,0.08);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.1);
      }

      .transaction-icon {
        font-size: 32px;
      }

      .transaction-info {
        flex: 1;
        margin-left: 16px;
      }

      .transaction-name {
        font-weight: 700;
        margin-bottom: 4px;
      }

      .transaction-date {
        font-size: 12px;
        color: var(--text-muted);
      }

      .transaction-amount {
        font-size: 18px;
        font-weight: 900;
      }

      .amount-positive {
        color: #10b981;
      }

      .amount-negative {
        color: #ef4444;
      }
    </style>

    <div style="max-width: 600px; margin: 0 auto;">
      <div class="balance-card">
        <div class="balance-label">Saldo Totale</div>
        <div class="balance-amount">€1.250,00</div>
      </div>

      <h3 style="margin-bottom: 16px; font-size: 20px;">Transazioni Recenti</h3>

      <div class="transactions">
        <div class="transaction">
          <div class="transaction-icon">🍕</div>
          <div class="transaction-info">
            <div class="transaction-name">Durger King</div>
            <div class="transaction-date">Oggi, 14:30</div>
          </div>
          <div class="transaction-amount amount-negative">-€27,50</div>
        </div>

        <div class="transaction">
          <div class="transaction-icon">💼</div>
          <div class="transaction-info">
            <div class="transaction-name">Stipendio</div>
            <div class="transaction-date">15 Nov</div>
          </div>
          <div class="transaction-amount amount-positive">+€2.500,00</div>
        </div>

        <div class="transaction">
          <div class="transaction-icon">☕</div>
          <div class="transaction-info">
            <div class="transaction-name">Caffè</div>
            <div class="transaction-date">14 Nov</div>
          </div>
          <div class="transaction-amount amount-negative">-€3,50</div>
        </div>
      </div>
    </div>
    """
    return get_base_template("Finanza", content, "finance")


def generate_psychology_page():
    """Pagina supporto psicologico"""
    content = """
    <div class="page-header">
      <h1>🧠 Supporto Psicologico</h1>
      <p>Il tuo benessere mentale conta</p>
    </div>

    <style>
      .mood-selector {
        display: flex;
        justify-content: space-around;
        padding: 24px;
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        margin-bottom: 24px;
      }

      .mood-btn {
        font-size: 48px;
        cursor: pointer;
        transition: all 0.3s ease;
        filter: grayscale(1);
        opacity: 0.5;
      }

      .mood-btn:active {
        transform: scale(1.3);
        filter: grayscale(0);
        opacity: 1;
      }

      .exercises {
        display: flex;
        flex-direction: column;
        gap: 16px;
      }

      .exercise-card {
        padding: 24px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
      }

      .exercise-card:active {
        transform: scale(0.98);
        background: rgba(99,102,241,0.2);
      }

      .exercise-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 12px;
      }

      .exercise-icon {
        font-size: 36px;
      }

      .exercise-title {
        font-size: 18px;
        font-weight: 700;
      }

      .exercise-desc {
        color: var(--text-muted);
        line-height: 1.6;
      }
    </style>

    <div style="max-width: 600px; margin: 0 auto;">
      <h3 style="margin-bottom: 16px;">Come ti senti oggi?</h3>

      <div class="mood-selector">
        <div class="mood-btn" onclick="selectMood('happy')">😊</div>
        <div class="mood-btn" onclick="selectMood('neutral')">😐</div>
        <div class="mood-btn" onclick="selectMood('sad')">😔</div>
        <div class="mood-btn" onclick="selectMood('anxious')">😰</div>
        <div class="mood-btn" onclick="selectMood('angry')">😠</div>
      </div>

      <h3 style="margin-bottom: 16px;">Esercizi Consigliati</h3>

      <div class="exercises">
        <div class="exercise-card" onclick="startExercise('breathing')">
          <div class="exercise-header">
            <div class="exercise-icon">🌬️</div>
            <div class="exercise-title">Respirazione Guidata</div>
          </div>
          <div class="exercise-desc">
            Esercizio di 5 minuti per ridurre lo stress e l'ansia
          </div>
        </div>

        <div class="exercise-card" onclick="startExercise('meditation')">
          <div class="exercise-header">
            <div class="exercise-icon">🧘</div>
            <div class="exercise-title">Meditazione</div>
          </div>
          <div class="exercise-desc">
            10 minuti di meditazione guidata per la calma interiore
          </div>
        </div>

        <div class="exercise-card" onclick="startExercise('journal')">
          <div class="exercise-header">
            <div class="exercise-icon">📝</div>
            <div class="exercise-title">Diario Emotivo</div>
          </div>
          <div class="exercise-desc">
            Scrivi i tuoi pensieri e emozioni del giorno
          </div>
        </div>
      </div>
    </div>

    <script>
      function selectMood(mood) {
        Telegram.WebApp.HapticFeedback.notificationOccurred('success');
        alert('Mood: ' + mood + ' registrato!');
      }

      function startExercise(type) {
        Telegram.WebApp.HapticFeedback.impactOccurred('medium');
        alert('Avvio esercizio: ' + type);
      }
    </script>
    """
    return get_base_template("Supporto", content, "psychology")


# Route handlers
async def home_handler(request):
    """Handler homepage"""
    return web.Response(text=generate_home_page(), content_type='text/html')


async def menu_handler(request):
    """Handler menu"""
    return web.Response(text=generate_menu_page(), content_type='text/html')


async def agent_handler(request):
    """Handler assistente"""
    return web.Response(text=generate_agent_page(), content_type='text/html')


async def finance_handler(request):
    """Handler finanza"""
    return web.Response(text=generate_finance_page(), content_type='text/html')


async def psychology_handler(request):
    """Handler psicologia"""
    return web.Response(text=generate_psychology_page(), content_type='text/html')


def setup_routes(app):
    """Configura tutte le route"""
    app.router.add_get('/', home_handler)
    app.router.add_get('/menu', menu_handler)
    app.router.add_get('/agent', agent_handler)
    app.router.add_get('/finance', finance_handler)
    app.router.add_get('/psychology', psychology_handler)