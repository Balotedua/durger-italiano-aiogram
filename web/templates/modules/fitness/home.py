# web/templates/modules/fitness/home.py
import sys
import os

sys.path.insert(0, os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from web.templates.base import get_base_template
from colors import (
    BG_DARK, BG_LIGHT, BG_LIGHTER, 
    TEXT, TEXT_ACCENT, TEXT_SECONDARY,
    PRIMARY, PRIMARY_LIGHT, PRIMARY_DARK,
    ACCENT_PRIMARY, BORDER_LIGHT
)


def generate_fitness_home():
    """Physical Wellness Hub - Ultra Premium Nero & Oro con SubNav"""

    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        body {{ 
            background: """ + BG_DARK + """ !important; 
            color: """ + TEXT + """ !important;
            font-family: 'Inter', sans-serif;
        }}

        .section-header {{
            text-align: center;
            padding: 40px 20px 30px;
        }}

        .section-title {{
            font-size: 32px;
            font-weight: 700;
            color: """ + PRIMARY + """;
            margin-bottom: 8px;
        }}

        .section-subtitle {{
            font-size: 16px;
            color: """ + TEXT_SECONDARY + """;
            max-width: 500px;
            margin: 0 auto;
            line-height: 1.5;
        }}

        .modules-grid {{
            max-width: 800px;
            margin: 0 auto;
            padding: 0 20px 40px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}

        .module-card {{
            background: """ + BG_LIGHT + """;
            border: 1px solid """ + BORDER_LIGHT + """;
            border-radius: 12px;
            padding: 24px;
            text-decoration: none;
            transition: all 0.2s ease;
            cursor: pointer;
        }}

        .module-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border-color: """ + ACCENT_PRIMARY + """;
        }}

        .module-icon {{
            font-size: 32px;
            margin-bottom: 16px;
        }}

        .module-title {{
            font-size: 18px;
            font-weight: 600;
            color: """ + PRIMARY + """;
            margin-bottom: 8px;
        }}

        .module-description {{
            font-size: 14px;
            color: """ + TEXT_SECONDARY + """;
            line-height: 1.5;
        }}

        .stats-section {{
            max-width: 800px;
            margin: 0 auto 40px;
            padding: 0 20px;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 16px;
        }}

        .stat-card {{
            background: """ + BG_LIGHT + """;
            border: 1px solid """ + BORDER_LIGHT + """;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 24px;
            font-weight: 700;
            color: """ + PRIMARY + """;
            margin-bottom: 4px;
        }}

        .stat-label {{
            font-size: 12px;
            color: """ + TEXT_SECONDARY + """;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
    </style>

    <div class="section-header">
        <h1 class="section-title">Physical Wellness</h1>
        <p class="section-subtitle">Monitora e migliora la tua forma fisica con strumenti professionali e dati precisi</p>
    </div>

    <div class="stats-section">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">12</div>
                <div class="stat-label">Workout Completati</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">85%</div>
                <div class="stat-label">Consistenza</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">-2.5kg</div>
                <div class="stat-label">Progresso</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">28</div>
                <div class="stat-label">Giorni Streak</div>
            </div>
        </div>
    </div>

    <div class="modules-grid">
        <a href="/workout" class="module-card">
            <div class="module-icon">🏋️</div>
            <h3 class="module-title">Allenamenti</h3>
            <p class="module-description">Programmi di allenamento personalizzati per obiettivi specifici</p>
        </a>

        <a href="/nutrition" class="module-card">
            <div class="module-icon">🥗</div>
            <h3 class="module-title">Nutrizione</h3>
            <p class="module-description">Piani alimentari e tracciamento calorie e macro</p>
        </a>

        <a href="/tracking" class="module-card">
            <div class="module-icon">📊</div>
            <h3 class="module-title">Progressi</h3>
            <p class="module-description">Monitora peso, misure e performance con grafici dettagliati</p>
        </a>

        <a href="/recovery" class="module-card">
            <div class="module-icon">🧘</div>
            <h3 class="module-title">Recupero</h3>
            <p class="module-description">Sonno, stretching e rigenerazione per massimizzare i risultati</p>
        </a>
    </div>

    <script>
        // Smooth interactions
        document.querySelectorAll('.module-card').forEach(card => {
            card.addEventListener('click', function(e) {
                // Optional: Add haptic feedback if in Telegram WebApp
                if (window.Telegram && Telegram.WebApp && Telegram.WebApp.HapticFeedback) {
                    Telegram.WebApp.HapticFeedback.impactOccurred('light');
                }
            });
        });
    </script>
    """

    return get_base_template("Physical Wellness", content, "fitness")
