# web/templates/modules/finance/home.py
import sys
import os

sys.path.insert(0, os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from web.templates.base import get_base_template
from colors import BG_DARK, GOLD, GOLD_LIGHT, GOLD_DARK, BG_LIGHT, TEXT


def generate_finance_home():
    """Finance Suite - Ultra Premium Nero & Oro"""

    content = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600&display=swap');

        body {{ background: {BG_DARK} !important; }}
        .bg-gradient {{
            background: radial-gradient(circle at 20% 50%, rgba(212,175,55,0.15) 0%, transparent 50%),
                        radial-gradient(circle at 80% 50%, rgba(212,175,55,0.1) 0%, transparent 50%) !important;
        }}

        /* Sub-Nav Premium Fissa */
        .finance-subnav {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(10,10,10,0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(212,175,55,0.2);
            padding: 16px 20px 12px;
            margin-bottom: 32px;
        }}

        .subnav-items {{
            display: flex;
            justify-content: space-around;
            max-width: 500px;
            margin: 0 auto;
            gap: 8px;
        }}

        .subnav-item {{
            flex: 1;
            text-align: center;
            padding: 14px 8px;
            border-radius: 18px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-decoration: none;
            position: relative;
            overflow: hidden;
        }}

        .subnav-item.active {{
            background: linear-gradient(135deg, rgba(212,175,55,0.2), rgba(212,175,55,0.1));
            border: 1px solid rgba(212,175,55,0.4);
            box-shadow: 0 8px 32px rgba(212,175,55,0.2);
        }}

        .subnav-icon {{
            font-size: 24px;
            margin-bottom: 6px;
            display: block;
        }}

        .subnav-label {{
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: {GOLD_LIGHT};
            opacity: 0.9;
        }}

        .subnav-item.active .subnav-label {{
            color: {GOLD};
            font-weight: 700;
        }}

        /* Header */
        .premium-header {{
            text-align: center;
            padding: 20px 20px 40px;
        }}

        .logo-icon {{
            font-size: 72px;
            filter: drop-shadow(0 8px 24px rgba(212,175,55,0.4));
            animation: float 6s ease-in-out infinite;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-12px); }}
        }}

        .app-name {{
            font-family: 'Playfair Display', serif;
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(135deg, {GOLD_LIGHT}, {GOLD}, {GOLD_DARK});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
            margin: 16px 0 8px;
        }}

        .tagline {{
            font-size: 15px;
            color: {GOLD_LIGHT};
            letter-spacing: 4px;
            text-transform: uppercase;
            opacity: 0.9;
        }}

        .divider {{
            width: 100px;
            height: 2px;
            background: linear-gradient(90deg, transparent, {GOLD}, transparent);
            margin: 32px auto;
        }}

        /* Balance Card */
        .balance-card {{
            background: linear-gradient(135deg, {BG_LIGHT}, rgba(212,175,55,0.15));
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 28px;
            padding: 40px 32px;
            text-align: center;
            margin: 0 20px 32px;
            box-shadow: 0 20px 60px rgba(212,175,55,0.2);
        }}

        .balance-label {{
            font-size: 14px;
            color: {GOLD_LIGHT};
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 12px;
        }}

        .balance-amount {{
            font-family: 'Playfair Display', serif;
            font-size: 56px;
            font-weight: 900;
            background: linear-gradient(135deg, {GOLD_LIGHT}, {GOLD});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 40px rgba(212,175,55,0.3);
        }}

        /* Quick Stats & Transactions */
        .cards-container {{
            max-width: 500px;
            margin: 0 auto;
            padding: 0 20px 40px;
        }}

        .premium-card {{
            position: relative;
            background: {BG_LIGHT};
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 24px;
            padding: 28px;
            margin-bottom: 20px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-decoration: none;
            display: block;
            overflow: hidden;
        }}

        /* Stessi effetti premium delle altre pagine */
        .premium-card::before, .premium-card::after {{ /* ... stessi effetti ... */ }}
        .premium-card:active {{ transform: translateY(-4px) scale(1.02); box-shadow: 0 20px 60px rgba(212,175,55,0.3); }}
        .premium-card:active::after {{ opacity: 1; }}

        .transaction-amount.positive {{ color: #10b981; }}
        .transaction-amount.negative {{ color: #ef4444; }}

        /* Particles */
        .gold-particle {{ /* ... stesso codice particles ... */ }}
    </style>

    <!-- Sub-Nav Premium -->
    <div class="finance-subnav">
        <div class="subnav-items">
            <a href="/finance" class="subnav-item active">
                <div class="subnav-icon">🏠</div>
                <div class="subnav-label">Home</div>
            </a>
            <a href="/finance/add" class="subnav-item">
                <div class="subnav-icon">➕</div>
                <div class="subnav-label">Aggiungi</div>
            </a>
            <a href="/finance/dashboard" class="subnav-item">
                <div class="subnav-icon">📊</div>
                <div class="subnav-label">Dashboard</div>
            </a>
            <a href="/finance/patrimonio" class="subnav-item">
                <div class="subnav-icon">💎</div>
                <div class="subnav-label">Patrimonio</div>
            </a>
        </div>
    </div>

    <div class="premium-header">
        <div class="logo-icon">💰</div>
        <h1 class="app-name">FINANCE SUITE</h1>
        <div class="tagline">IL TUO PATRIMONIO, IL TUO POTERE</div>
        <div class="divider"></div>
    </div>

    <!-- Balance Card -->
    <div class="balance-card">
        <div class="balance-label">Saldo Totale</div>
        <div class="balance-amount">€1.250,00</div>
    </div>

    <div class="cards-container">
        <!-- Puoi aggiungere altre card premium qui se vuoi -->
    </div>

    <script>
        // Particelle oro
        function createGoldParticles() {{
            for (let i = 0; i < 18; i++) {{
                const p = document.createElement('div');
                p.className = 'gold-particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.animationDuration = (Math.random() * 10 + 8) + 's';
                p.style.animationDelay = Math.random() * 5 + 's';
                document.body.appendChild(p);
            }}
        }}
        createGoldParticles();

        // Haptic su subnav e card
        document.querySelectorAll('a').forEach(link => {{
            link.addEventListener('click', function(e) {{
                Telegram.WebApp.HapticFeedback.impactOccurred('medium');
            }});
        }});
    </script>
    """

    return get_base_template("Finance Suite", content, "finance")
