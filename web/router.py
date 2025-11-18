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


# Aggiungi questa funzione in web/router.py al posto di generate_home_page()

def generate_home_page():
    """Homepage ULTRA PREMIUM - Nero & Oro"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #F4E5B2;
            --gold-dark: #9B7F1B;
            --black: #0A0A0A;
            --black-light: #1A1A1A;
            --black-lighter: #2A2A2A;
            --white: #FFFFFF;
        }

        /* Override base styles */
        body {
            background: var(--black) !important;
        }

        .bg-gradient {
            background: radial-gradient(circle at 20% 50%, rgba(212,175,55,0.15) 0%, transparent 50%),
                        radial-gradient(circle at 80% 50%, rgba(212,175,55,0.1) 0%, transparent 50%) !important;
            opacity: 1 !important;
        }

        /* HEADER PREMIUM */
        .premium-header {
            text-align: center;
            padding: 60px 20px 40px;
            position: relative;
        }

        .logo-container {
            margin-bottom: 24px;
            animation: fadeInDown 0.8s ease;
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .logo-icon {
            font-size: 72px;
            filter: drop-shadow(0 8px 24px rgba(212,175,55,0.4));
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-12px); }
        }

        .app-name {
            font-family: 'Playfair Display', serif;
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold-light), var(--gold), var(--gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
            margin-bottom: 12px;
            text-shadow: 0 0 40px rgba(212,175,55,0.3);
            animation: fadeInUp 0.8s ease 0.2s backwards;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .tagline {
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            font-weight: 500;
            color: var(--gold-light);
            letter-spacing: 4px;
            text-transform: uppercase;
            opacity: 0.9;
            animation: fadeInUp 0.8s ease 0.4s backwards;
        }

        .divider {
            width: 60px;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            margin: 32px auto;
            animation: fadeInUp 0.8s ease 0.6s backwards;
        }

        /* CARDS PREMIUM */
        .cards-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .premium-card {
            position: relative;
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 24px;
            padding: 32px 28px;
            margin-bottom: 20px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-decoration: none;
            display: block;
            overflow: hidden;
            animation: fadeInUp 0.8s ease backwards;
        }

        .premium-card:nth-child(1) { animation-delay: 0.8s; }
        .premium-card:nth-child(2) { animation-delay: 1s; }
        .premium-card:nth-child(3) { animation-delay: 1.2s; }
        .premium-card:nth-child(4) { animation-delay: 1.4s; }

        .premium-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(212,175,55,0.1), transparent);
            transition: left 0.6s ease;
        }

        .premium-card:active::before {
            left: 100%;
        }

        .premium-card::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 24px;
            padding: 1px;
            background: linear-gradient(135deg, var(--gold), transparent, var(--gold));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0;
            transition: opacity 0.4s;
        }

        .premium-card:active {
            transform: translateY(-4px) scale(1.02);
            border-color: rgba(212,175,55,0.5);
            box-shadow: 0 20px 60px rgba(212,175,55,0.3);
        }

        .premium-card:active::after {
            opacity: 1;
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 16px;
        }

        .card-icon-container {
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, rgba(212,175,55,0.15), rgba(212,175,55,0.05));
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.4s ease;
        }

        .premium-card:active .card-icon-container {
            transform: scale(1.1) rotate(5deg);
            background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15));
            border-color: rgba(212,175,55,0.6);
        }

        .card-icon {
            font-size: 36px;
            filter: drop-shadow(0 4px 12px rgba(212,175,55,0.3));
        }

        .card-content {
            flex: 1;
        }

        .card-title {
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 700;
            color: var(--gold-light);
            margin-bottom: 4px;
            letter-spacing: -0.5px;
        }

        .card-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            font-weight: 500;
            color: rgba(212,175,55,0.7);
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .card-description {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 400;
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
            margin-top: 12px;
        }

        .card-arrow {
            position: absolute;
            right: 24px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 24px;
            color: var(--gold);
            opacity: 0.5;
            transition: all 0.4s ease;
        }

        .premium-card:active .card-arrow {
            opacity: 1;
            transform: translateY(-50%) translateX(8px);
        }

        /* FOOTER INFO */
        .footer-info {
            text-align: center;
            padding: 40px 20px 20px;
            animation: fadeIn 1s ease 1.6s backwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .footer-text {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: rgba(212,175,55,0.5);
            letter-spacing: 1px;
        }

        /* Particles oro */
        .gold-particle {
            position: fixed;
            width: 3px;
            height: 3px;
            background: var(--gold);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            opacity: 0;
            animation: particle-float linear infinite;
        }

        @keyframes particle-float {
            0% {
                opacity: 0;
                transform: translateY(100vh) scale(0);
            }
            10% {
                opacity: 0.8;
            }
            90% {
                opacity: 0.8;
            }
            100% {
                opacity: 0;
                transform: translateY(-20vh) scale(1);
            }
        }
    </style>

    <div class="premium-header">
        <div class="logo-container">
            <div class="logo-icon">👑</div>
        </div>
        <h1 class="app-name">DANISON ASSISTANT</h1>
        <div class="tagline">UN DANISON CHE TI ASSISTE 24/7</div>
        <div class="divider"></div>
    </div>

    <div class="cards-container">
        <a href="/menu" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container">
                    <div class="card-icon">🍕</div>
                </div>
                <div class="card-content">
                    <div class="card-title">Gourmet Menu</div>
                    <div class="card-subtitle">Italian Cuisine</div>
                </div>
            </div>
            <div class="card-description">
                Esplora il nostro menu esclusivo di specialità italiane premium
            </div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/agent" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container">
                    <div class="card-icon">🤖</div>
                </div>
                <div class="card-content">
                    <div class="card-title">AI Assistant</div>
                    <div class="card-subtitle">24/7 Support</div>
                </div>
            </div>
            <div class="card-description">
                Assistente personale intelligente sempre al tuo servizio
            </div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/finance" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container">
                    <div class="card-icon">💰</div>
                </div>
                <div class="card-content">
                    <div class="card-title">Finance Suite</div>
                    <div class="card-subtitle">Wealth Management</div>
                </div>
            </div>
            <div class="card-description">
                Gestisci il tuo patrimonio con strumenti professionali
            </div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/psychology" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container">
                    <div class="card-icon">🧠</div>
                </div>
                <div class="card-content">
                    <div class="card-title">Wellness Hub</div>
                    <div class="card-subtitle">Mental Health</div>
                </div>
            </div>
            <div class="card-description">
                Centro benessere per la tua salute mentale ed emotiva
            </div>
            <div class="card-arrow">→</div>
        </a>
    </div>

    <div class="footer-info">
        <div class="footer-text">DANISON MENU</div>
    </div>

    <script>
        // Crea particelle oro animate
        function createGoldParticles() {
            for (let i = 0; i < 15; i++) {
                const particle = document.createElement('div');
                particle.className = 'gold-particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDuration = (Math.random() * 8 + 6) + 's';
                particle.style.animationDelay = Math.random() * 5 + 's';
                document.body.appendChild(particle);
            }
        }

        createGoldParticles();

        // Haptic feedback premium
        document.querySelectorAll('.premium-card').forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                Telegram.WebApp.HapticFeedback.impactOccurred('heavy');

                setTimeout(() => {
                    window.location.href = this.getAttribute('href');
                }, 300);
            });
        });
    </script>
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