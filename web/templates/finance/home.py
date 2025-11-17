# web/templates/modules/finance/home.py
import sys
import os

sys.path.insert(0, os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from web.templates.base import get_base_template


def generate_finance_home():
    """Homepage Finanza con overview"""

    # Sub-navbar per Finanza
    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': False},
        {'url': '/finance/dashboard', 'label': 'Dashboard', 'icon': '📊', 'active': False},
        {'url': '/finance/patrimonio', 'label': 'Patrimonio', 'icon': '💎', 'active': False},
    ]

    content = """
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

        .quick-stats {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-card {
            padding: 20px;
            background: rgba(255,255,255,0.08);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .stat-label {
            font-size: 12px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }

        .stat-value {
            font-size: 24px;
            font-weight: 900;
        }

        .stat-positive {
            color: #10b981;
        }

        .stat-negative {
            color: #ef4444;
        }

        .recent-title {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 16px;
        }

        .transaction {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px;
            background: rgba(255,255,255,0.08);
            border-radius: 16px;
            margin-bottom: 12px;
        }

        .transaction-icon {
            font-size: 32px;
            margin-right: 12px;
        }

        .transaction-info {
            flex: 1;
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
    </style>

    <div style="max-width: 600px; margin: 0 auto;">
        <div class="page-header">
            <h1>💰 Finanza Personale</h1>
            <p>Gestisci il tuo budget</p>
        </div>

        <div class="balance-card">
            <div class="balance-label">Saldo Totale</div>
            <div class="balance-amount">€1.250,00</div>
        </div>

        <div class="quick-stats">
            <div class="stat-card">
                <div class="stat-label">Entrate Mese</div>
                <div class="stat-value stat-positive">+€2.500</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Uscite Mese</div>
                <div class="stat-value stat-negative">-€1.250</div>
            </div>
        </div>

        <div class="recent-title">Transazioni Recenti</div>

        <div class="transaction">
            <div style="display: flex; align-items: center;">
                <div class="transaction-icon">🍕</div>
                <div class="transaction-info">
                    <div class="transaction-name">Durger King</div>
                    <div class="transaction-date">Oggi, 14:30</div>
                </div>
            </div>
            <div class="transaction-amount stat-negative">-€27,50</div>
        </div>

        <div class="transaction">
            <div style="display: flex; align-items: center;">
                <div class="transaction-icon">💼</div>
                <div class="transaction-info">
                    <div class="transaction-name">Stipendio</div>
                    <div class="transaction-date">15 Nov</div>
                </div>
            </div>
            <div class="transaction-amount stat-positive">+€2.500,00</div>
        </div>

        <div class="transaction">
            <div style="display: flex; align-items: center;">
                <div class="transaction-icon">☕</div>
                <div class="transaction-info">
                    <div class="transaction-name">Caffè</div>
                    <div class="transaction-date">14 Nov</div>
                </div>
            </div>
            <div class="transaction-amount stat-negative">-€3,50</div>
        </div>
    </div>
    """

    return get_base_template("Finanza", content, "finance", sub_nav)