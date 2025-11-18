# web/templates/modules/finance/add_payment.py
import sys
import os

sys.path.insert(0, os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from web.templates.base import get_base_template


def generate_add_payment():
    """Pagina Aggiungi Pagamento"""

    sub_nav = [
        {'url': '/finance', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/finance/add', 'label': 'Aggiungi', 'icon': '➕', 'active': True},
        {'url': '/finance/dashboard', 'label': 'Dashboard', 'icon': '📊', 'active': False},
        {'url': '/finance/patrimonio', 'label': 'Patrimonio', 'icon': '💎', 'active': False},
    ]

    content = """
    <style>
        .form-container {
            max-width: 500px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--text-muted);
        }

        .form-input, .form-select {
            width: 100%;
            padding: 16px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            color: white;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
        }

        .form-input:focus, .form-select:focus {
            background: rgba(255,255,255,0.12);
            border-color: var(--primary);
        }

        .type-selector {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }

        .type-btn {
            padding: 20px;
            background: rgba(255,255,255,0.08);
            border: 2px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .type-btn:active {
            transform: scale(0.98);
        }

        .type-btn.active {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-color: transparent;
        }

        .type-icon {
            font-size: 32px;
            margin-bottom: 8px;
        }

        .type-label {
            font-weight: 700;
        }

        .submit-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border: none;
            border-radius: 20px;
            color: white;
            font-size: 18px;
            font-weight: 900;
            cursor: pointer;
            text-transform: uppercase;
            transition: all 0.3s ease;
        }

        .submit-btn:active {
            transform: scale(0.98);
        }

        .quick-amounts {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-top: 12px;
        }

        .quick-amount {
            padding: 12px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            text-align: center;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s ease;
        }

        .quick-amount:active {
            transform: scale(0.95);
            background: rgba(99,102,241,0.2);
        }
    </style>

    <div class="form-container">
        <div class="page-header">
            <h1>➕ Aggiungi Transazione</h1>
            <p>Registra entrate o uscite</p>
        </div>

        <div class="type-selector">
            <div class="type-btn active" id="typeIncome" onclick="selectType('income')">
                <div class="type-icon">💰</div>
                <div class="type-label">Entrata</div>
            </div>
            <div class="type-btn" id="typeExpense" onclick="selectType('expense')">
                <div class="type-icon">💸</div>
                <div class="type-label">Uscita</div>
            </div>
        </div>

        <form id="transactionForm">
            <div class="form-group">
                <label class="form-label">Importo (€)</label>
                <input type="number" class="form-input" id="amount" placeholder="0,00" step="0.01" required>
                <div class="quick-amounts">
                    <div class="quick-amount" onclick="setAmount(10)">€10</div>
                    <div class="quick-amount" onclick="setAmount(50)">€50</div>
                    <div class="quick-amount" onclick="setAmount(100)">€100</div>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">Categoria</label>
                <select class="form-select" id="category" required>
                    <option value="">Seleziona...</option>
                    <option value="food">🍕 Cibo</option>
                    <option value="transport">🚗 Trasporti</option>
                    <option value="entertainment">🎬 Svago</option>
                    <option value="shopping">🛍️ Shopping</option>
                    <option value="bills">📄 Bollette</option>
                    <option value="salary">💼 Stipendio</option>
                    <option value="other">❓ Altro</option>
                </select>
            </div>

            <div class="form-group">
                <label class="form-label">Descrizione</label>
                <input type="text" class="form-input" id="description" placeholder="Es: Spesa supermercato" required>
            </div>

            <div class="form-group">
                <label class="form-label">Data</label>
                <input type="date" class="form-input" id="date" required>
            </div>

            <button type="submit" class="submit-btn">Aggiungi Transazione</button>
        </form>
    </div>

    <script>
        let selectedType = 'income';

        function selectType(type) {
            selectedType = type;
            document.getElementById('typeIncome').classList.toggle('active', type === 'income');
            document.getElementById('typeExpense').classList.toggle('active', type === 'expense');
            Telegram.WebApp.HapticFeedback.impactOccurred('light');
        }

        function setAmount(value) {
            document.getElementById('amount').value = value;
            Telegram.WebApp.HapticFeedback.impactOccurred('light');
        }

        // Set today's date
        document.getElementById('date').valueAsDate = new Date();

        document.getElementById('transactionForm').addEventListener('submit', function(e) {
            e.preventDefault();

            const data = {
                type: selectedType,
                amount: document.getElementById('amount').value,
                category: document.getElementById('category').value,
                description: document.getElementById('description').value,
                date: document.getElementById('date').value
            };

            Telegram.WebApp.HapticFeedback.notificationOccurred('success');
            Telegram.WebApp.showAlert('Transazione aggiunta con successo!');

            // Reset form
            this.reset();
            document.getElementById('date').valueAsDate = new Date();
        });
    </script>
    """

    return get_base_template("Aggiungi Pagamento", content, "finance", sub_nav)