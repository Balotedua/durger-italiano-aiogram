# web/router.py - Router con sub-routes modulari
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiohttp import web
from web.templates.base import get_base_template
from web.templates.agent import generate_agent_page

# Import moduli finanza
from web.templates.finance.home import generate_finance_home
from web.templates.finance.add_payment import generate_add_payment


# ==== FUNZIONI DI GENERAZIONE PAGINE ====

def generate_home_page():
    """Homepage ULTRA PREMIUM - Nero & Oro"""
    content = """
    <div class="page-header">
        <h1>🏠 Home</h1>
        <p>Benvenuto nell'assistente Danison</p>
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

# ==== NUOVE FUNZIONI ====
def generate_dashboard_page():
    content = "<div class='page-header'><h1>📊 Dashboard</h1><p>Panoramica generale...</p></div>"
    return get_base_template("Dashboard", content, "dashboard")

def generate_badge_page():
    content = "<div class='page-header'><h1>🎖️ Badge</h1><p>I tuoi traguardi...</p></div>"
    return get_base_template("Badge", content, "badge")

def generate_career_page():
    content = "<div class='page-header'><h1>💼 Career</h1><p>Gestione carriera...</p></div>"
    return get_base_template("Career", content, "career")

def generate_jolly_page():
    content = "<div class='page-header'><h1>🎭 Jolly</h1><p>Attività casuali...</p></div>"
    return get_base_template("Jolly", content, "jolly")

def generate_mental_health_page():
    content = "<div class='page-header'><h1>🧠 Salute Mentale</h1><p>Benessere mentale...</p></div>"
    return get_base_template("Salute Mentale", content, "mental-health")

def generate_detox_page():
    content = "<div class='page-header'><h1>🌿 Detox Social</h1><p>Stacca dai social...</p></div>"
    return get_base_template("Detox", content, "detox")

def generate_fitness_page():
    content = "<div class='page-header'><h1>💪 Allenamenti</h1><p>Salute fisica...</p></div>"
    return get_base_template("Fitness", content, "fitness")

def generate_time_management_page():
    content = "<div class='page-header'><h1>⏰ Gestione Tempo</h1><p>Organizza il tempo...</p></div>"
    return get_base_template("Gestione Tempo", content, "time-management")

def generate_news_page():
    content = "<div class='page-header'><h1>📰 News Skill</h1><p>Aggiornamenti...</p></div>"
    return get_base_template("News", content, "news")

def generate_notes_page():
    content = "<div class='page-header'><h1>📝 Note</h1><p>Appunti personali...</p></div>"
    return get_base_template("Note", content, "notes")

# ==== HANDLERS SEMPLIFICATI ====

async def home_handler(request):
    return web.Response(text=generate_home_page(), content_type='text/html')

async def menu_handler(request):
    return web.Response(text=generate_menu_page(), content_type='text/html')

async def agent_handler(request):
    return web.Response(text=generate_agent_page(), content_type='text/html')

async def psychology_handler(request):
    return web.Response(text=generate_psychology_page(), content_type='text/html')

# Finanza handlers
async def finance_home_handler(request):
    return web.Response(text=generate_finance_home(), content_type='text/html')

async def finance_add_handler(request):
    return web.Response(text=generate_add_payment(), content_type='text/html')

async def finance_dashboard_handler(request):
    content = "<div class='page-header'><h1>📊 Dashboard</h1><p>Grafici e statistiche...</p></div>"
    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        {'url': '/finance/dashboard', 'label': 'Dashboard', 'icon': '📊', 'active': True},
    ]
    return web.Response(text=get_base_template("Dashboard Finanza", content, "finance", sub_nav), content_type='text/html')

async def finance_patrimonio_handler(request):
    content = "<div class='page-header'><h1>💎 Patrimonio</h1><p>Gestione patrimonio...</p></div>"
    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        {'url': '/finance/patrimonio', 'label': 'Patrimonio', 'icon': '💎', 'active': True},
    ]
    return web.Response(text=get_base_template("Patrimonio", content, "finance", sub_nav), content_type='text/html')

# Nuovi handlers
async def dashboard_handler(request):
    return web.Response(text=generate_dashboard_page(), content_type='text/html')

async def badge_handler(request):
    return web.Response(text=generate_badge_page(), content_type='text/html')

async def career_handler(request):
    return web.Response(text=generate_career_page(), content_type='text/html')

async def jolly_handler(request):
    return web.Response(text=generate_jolly_page(), content_type='text/html')

async def mental_health_handler(request):
    return web.Response(text=generate_mental_health_page(), content_type='text/html')

async def detox_handler(request):
    return web.Response(text=generate_detox_page(), content_type='text/html')

async def fitness_handler(request):
    return web.Response(text=generate_fitness_page(), content_type='text/html')

async def time_management_handler(request):
    return web.Response(text=generate_time_management_page(), content_type='text/html')

async def news_handler(request):
    return web.Response(text=generate_news_page(), content_type='text/html')

async def notes_handler(request):
    return web.Response(text=generate_notes_page(), content_type='text/html')

def setup_routes(app):
    """Configura tutte le route"""
    # Main routes
    app.router.add_get('/', home_handler)
    app.router.add_get('/menu', menu_handler)
    app.router.add_get('/agent', agent_handler)
    app.router.add_get('/psychology', psychology_handler)

    # Finance routes
    app.router.add_get('/finance', finance_home_handler)
    app.router.add_get('/finance/add', finance_add_handler)
    app.router.add_get('/finance/dashboard', finance_dashboard_handler)
    app.router.add_get('/finance/patrimonio', finance_patrimonio_handler)

    # Nuove routes
    app.router.add_get('/dashboard', dashboard_handler)
    app.router.add_get('/badge', badge_handler)
    app.router.add_get('/career', career_handler)
    app.router.add_get('/jolly', jolly_handler)
    app.router.add_get('/mental-health', mental_health_handler)
    app.router.add_get('/detox', detox_handler)
    app.router.add_get('/fitness', fitness_handler)
    app.router.add_get('/time-management', time_management_handler)
    app.router.add_get('/news', news_handler)
    app.router.add_get('/notes', notes_handler)