# web/router_pages/homepage.py - Homepage Premium
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate():
    """Homepage Dashboard con overview di tutto"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&display=swap');

        .welcome {{
            text-align: center;
            padding: 60px 20px 40px;
        }}

        .logo {{
            font-size: 80px;
            margin-bottom: 20px;
            filter: drop-shadow(0 8px 24px rgba(212,175,55,0.4));
            animation: float 4s ease-in-out infinite;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-12px); }}
        }}

        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 900;
            background: linear-gradient(135deg, #f4e4a0, #d4af37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        .tagline {{
            color: rgba(212,175,55,0.8);
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-weight: 700;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin: 32px 0;
        }}

        .stat-card {{
            padding: 20px;
            background: rgba(212,175,55,0.08);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 20px;
            text-align: center;
            transition: all 0.3s ease;
        }}

        .stat-card:active {{
            transform: scale(0.97);
            background: rgba(212,175,55,0.12);
        }}

        .stat-value {{
            font-size: 28px;
            font-weight: 900;
            color: #d4af37;
            margin-bottom: 4px;
        }}

        .stat-label {{
            font-size: 12px;
            color: rgba(255,255,255,0.6);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .quick-actions {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 24px;
        }}

        .quick-btn {{
            padding: 24px 12px;
            background: rgba(13,13,13,0.6);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 18px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
        }}

        .quick-btn:active {{
            transform: scale(0.95);
            background: rgba(212,175,55,0.15);
            border-color: rgba(212,175,55,0.5);
        }}

        .quick-icon {{
            font-size: 32px;
            margin-bottom: 8px;
            display: block;
        }}

        .quick-label {{
            font-size: 11px;
            font-weight: 700;
            color: rgba(212,175,55,0.9);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .section-title {{
            font-size: 16px;
            font-weight: 700;
            color: #d4af37;
            margin: 32px 0 16px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
    </style>

    <div class="welcome">
        <div class="logo">👑</div>
        <h1>DURGER KING</h1>
        <div class="tagline">Your Life Assistant</div>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-value">€1.250</div>
            <div class="stat-label">Saldo</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">5</div>
            <div class="stat-label">Badge</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">87%</div>
            <div class="stat-label">Obiettivi</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">😊</div>
            <div class="stat-label">Mood</div>
        </div>
    </div>

    <div class="section-title">⚡ Quick Actions</div>

    <div class="quick-actions">
        <a href="/finance/add" class="quick-btn">
            <span class="quick-icon">💰</span>
            <div class="quick-label">Aggiungi €</div>
        </a>
        <a href="/notes" class="quick-btn">
            <span class="quick-icon">📝</span>
            <div class="quick-label">Note</div>
        </a>
        <a href="/mental/mood" class="quick-btn">
            <span class="quick-icon">🧠</span>
            <div class="quick-label">Mood</div>
        </a>
        <a href="/fitness/workouts" class="quick-btn">
            <span class="quick-icon">💪</span>
            <div class="quick-label">Workout</div>
        </a>
        <a href="/time/routines" class="quick-btn">
            <span class="quick-icon">⏰</span>
            <div class="quick-label">Routine</div>
        </a>
        <a href="/agent" class="quick-btn">
            <span class="quick-icon">🤖</span>
            <div class="quick-label">AI Agent</div>
        </a>
    </div>

    <div class="section-title">📊 Oggi</div>

    <div style="padding:20px; background:rgba(212,175,55,0.05); border:1px solid rgba(212,175,55,0.2); border-radius:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <span style="color:rgba(255,255,255,0.7);">💪 Allenamento</span>
            <span style="color:#d4af37; font-weight:700;">Completato</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <span style="color:rgba(255,255,255,0.7);">📝 Note scritte</span>
            <span style="color:#d4af37; font-weight:700;">3</span>
        </div>
        <div style="display:flex; justify-content:space-between;">
            <span style="color:rgba(255,255,255,0.7);">🌿 Detox social</span>
            <span style="color:#d4af37; font-weight:700;">2h 15m</span>
        </div>
    </div>

    <script>
        // Haptic feedback
        document.querySelectorAll('.quick-btn, .stat-card').forEach(el => {
            el.addEventListener('click', () => {
                Telegram.WebApp.HapticFeedback.impactOccurred('light');
            });
        });
    </script>
    """
    return get_base_template("Home", content, "home")