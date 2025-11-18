# web/router.py - Router COMPLETO con tutte le sezioni
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiohttp import web
from web.templates.base import get_base_template
from web.templates.agent import generate_agent_page

# Import moduli esistenti
try:
    from web.templates.modules.finance.home import generate_finance_home
    from web.templates.modules.finance.add_payment import generate_add_payment
except:
    pass


def generate_home_page():
    """Homepage Dashboard"""
    from web.router_pages import homepage
    return homepage.generate()


def generate_menu_page():
    """Menu ristorante"""
    try:
        from web.templates.menu import generate_menu_html
        return generate_menu_html()
    except:
        return get_base_template("Menu", "<p>Menu in arrivo...</p>", "menu")


# ========== PLACEHOLDER PAGES ==========

def placeholder_page(title, icon, active_key, sections=None):
    """Genera pagina placeholder con sub-menu"""
    sub_nav = sections if sections else None
    content = f'''
    <div style="text-align:center; padding:60px 20px;">
        <div style="font-size:80px; margin-bottom:24px;">{icon}</div>
        <h1 style="font-family:'Playfair Display',serif; font-size:32px; background:linear-gradient(135deg,#f4e4a0,#d4af37); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:12px;">{title}</h1>
        <p style="color:rgba(255,255,255,0.6); font-size:15px;">Sezione in costruzione...</p>
    </div>
    '''
    return get_base_template(title, content, active_key, sub_nav)


# ========== HANDLERS ==========

async def home_handler(request):
    return web.Response(text=generate_home_page(), content_type='text/html')


async def menu_handler(request):
    return web.Response(text=generate_menu_page(), content_type='text/html')


async def agent_handler(request):
    return web.Response(text=generate_agent_page(), content_type='text/html')


# RECAP
async def recap_handler(request):
    sub_nav = [
        {'url': '/recap', 'label': 'Overview', 'icon': '📊', 'active': True},
        {'url': '/recap/stats', 'label': 'Statistiche', 'icon': '📈', 'active': False},
    ]
    return web.Response(text=placeholder_page("Dashboard Recap", "📊", "recap", sub_nav), content_type='text/html')


# CAREER
async def career_handler(request):
    sub_nav = [
        {'url': '/career', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/career/badges', 'label': 'Badge', 'icon': '🎖️', 'active': False},
        {'url': '/career/goals', 'label': 'Obiettivi', 'icon': '🎯', 'active': False},
    ]
    return web.Response(text=placeholder_page("Badge & Career", "🎖️", "career", sub_nav), content_type='text/html')


# TIME MANAGEMENT
async def time_handler(request):
    sub_nav = [
        {'url': '/time', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/time/routines', 'label': 'Routine', 'icon': '🔄', 'active': False},
        {'url': '/time/calendar', 'label': 'Calendario', 'icon': '📅', 'active': False},
    ]
    return web.Response(text=placeholder_page("Gestione Tempo", "⏰", "time", sub_nav), content_type='text/html')


# NOTES
async def notes_handler(request):
    return web.Response(text=placeholder_page("Note", "📝", "notes"), content_type='text/html')


# MENTAL HEALTH
async def mental_handler(request):
    sub_nav = [
        {'url': '/mental', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/mental/mood', 'label': 'Mood', 'icon': '😊', 'active': False},
        {'url': '/mental/exercises', 'label': 'Esercizi', 'icon': '🧘', 'active': False},
    ]
    return web.Response(text=placeholder_page("Salute Mentale", "🧠", "mental", sub_nav), content_type='text/html')


# FITNESS
async def fitness_handler(request):
    sub_nav = [
        {'url': '/fitness', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/fitness/workouts', 'label': 'Allenamenti', 'icon': '🏋️', 'active': False},
        {'url': '/fitness/nutrition', 'label': 'Nutrizione', 'icon': '🥗', 'active': False},
    ]
    return web.Response(text=placeholder_page("Fitness", "💪", "fitness", sub_nav), content_type='text/html')


# DETOX
async def detox_handler(request):
    return web.Response(text=placeholder_page("Detox Digitale", "🌿", "detox"), content_type='text/html')


# FINANCE
async def finance_home_handler(request):
    try:
        return web.Response(text=generate_finance_home(), content_type='text/html')
    except:
        sub_nav = [
            {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': True},
            {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        ]
        return web.Response(text=placeholder_page("Finanza", "💰", "finance", sub_nav), content_type='text/html')


async def finance_add_handler(request):
    try:
        return web.Response(text=generate_add_payment(), content_type='text/html')
    except:
        return web.Response(text=placeholder_page("Aggiungi Pagamento", "💰", "finance"), content_type='text/html')


# JOLLY
async def jolly_handler(request):
    return web.Response(text=placeholder_page("Jolly", "🃏", "jolly"), content_type='text/html')


# NEWS
async def news_handler(request):
    return web.Response(text=placeholder_page("News & Skills", "📰", "news"), content_type='text/html')


def setup_routes(app):
    """Configura TUTTE le route"""
    # Main
    app.router.add_get('/', home_handler)
    app.router.add_get('/menu', menu_handler)
    app.router.add_get('/agent', agent_handler)

    # Nuove sezioni
    app.router.add_get('/recap', recap_handler)
    app.router.add_get('/career', career_handler)
    app.router.add_get('/time', time_handler)
    app.router.add_get('/notes', notes_handler)
    app.router.add_get('/mental', mental_handler)
    app.router.add_get('/fitness', fitness_handler)
    app.router.add_get('/detox', detox_handler)
    app.router.add_get('/jolly', jolly_handler)
    app.router.add_get('/news', news_handler)

    # Finance
    app.router.add_get('/finance', finance_home_handler)
    app.router.add_get('/finance/add', finance_add_handler)


import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiohttp import web
from web.templates.base import get_base_template
from web.templates.agent import generate_agent_page

# Import moduli finanza
from web.templates.modules.finance.home import generate_finance_home
from web.templates.modules.finance.add_payment import generate_add_payment


def generate_home_page():
    """Homepage"""
    content = """
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

    <div class="page-header">
        <h1>🏠 Durger King</h1>
        <p>La tua app completa</p>
    </div>

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
            <div class="feature-desc">Gestisci budget</div>
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
    """Menu page"""
    try:
        from web.templates.menu import generate_menu_html
        return generate_menu_html()
    except ImportError:
        return get_base_template("Menu", "<p>Menu non disponibile</p>", "menu")


def generate_psychology_page():
    """Psychology placeholder"""
    content = "<div class='page-header'><h1>🧠 Supporto Psicologico</h1><p>In arrivo...</p></div>"
    return get_base_template("Supporto", content, "psychology")


# ==== ROUTE HANDLERS ====

async def home_handler(request):
    return web.Response(text=generate_home_page(), content_type='text/html')


async def menu_handler(request):
    return web.Response(text=generate_menu_page(), content_type='text/html')


async def agent_handler(request):
    return web.Response(text=generate_agent_page(), content_type='text/html')


# FINANZA ROUTES
async def finance_home_handler(request):
    return web.Response(text=generate_finance_home(), content_type='text/html')


async def finance_add_handler(request):
    return web.Response(text=generate_add_payment(), content_type='text/html')


async def finance_dashboard_handler(request):
    content = "<div class='page-header'><h1>📊 Dashboard</h1><p>Grafici e statistiche in arrivo...</p></div>"
    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        {'url': '/finance/dashboard', 'label': 'Dashboard', 'icon': '📊', 'active': True},
        {'url': '/finance/patrimonio', 'label': 'Patrimonio', 'icon': '💎', 'active': False},
    ]
    return web.Response(text=get_base_template("Dashboard", content, "finance", sub_nav), content_type='text/html')


async def finance_patrimonio_handler(request):
    content = "<div class='page-header'><h1>💎 Patrimonio</h1><p>Gestione patrimonio in arrivo...</p></div>"
    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        {'url': '/finance/dashboard', 'label': 'Dashboard', 'icon': '📊', 'active': False},
        {'url': '/finance/patrimonio', 'label': 'Patrimonio', 'icon': '💎', 'active': True},
    ]
    return web.Response(text=get_base_template("Patrimonio", content, "finance", sub_nav), content_type='text/html')


# PSYCHOLOGY ROUTES
async def psychology_handler(request):
    return web.Response(text=generate_psychology_page(), content_type='text/html')


def setup_routes(app):
    """Configura tutte le route con sub-routes"""
    # Main routes
    app.router.add_get('/', home_handler)
    app.router.add_get('/menu', menu_handler)
    app.router.add_get('/agent', agent_handler)

    # Finance sub-routes
    app.router.add_get('/finance', finance_home_handler)
    app.router.add_get('/finance/add', finance_add_handler)
    app.router.add_get('/finance/dashboard', finance_dashboard_handler)
    app.router.add_get('/finance/patrimonio', finance_patrimonio_handler)

    # Psychology sub-routes
    app.router.add_get('/psychology', psychology_handler)
    # Puoi aggiungere: /psychology/diary, /psychology/exercises, ecc.