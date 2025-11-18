def generate_fitness_home():
    """Homepage Salute Fisica - Stile Nero & Oro"""
    content = """
    <style>
        .fitness-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 24px;
        }
        
        .stat-card {
            background: rgba(212,175,55,0.1);
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 24px;
            font-weight: 700;
            color: #D4AF37;
            margin-bottom: 4px;
        }
        
        .stat-label {
            font-size: 12px;
            color: rgba(255,255,255,0.7);
        }
    </style>

    <div class="page-header">
        <h1>💪 Salute Fisica</h1>
        <p>Allenamenti e benessere fisico</p>
    </div>

    <div class="fitness-stats">
        <div class="stat-card">
            <div class="stat-value">12</div>
            <div class="stat-label">Allenamenti</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">85%</div>
            <div class="stat-label">Completati</div>
        </div>
    </div>

    <div class="card">
        <h3>I tuoi Allenamenti</h3>
        <p>Gestisci la tua routine di allenamento...</p>
        <a href="/fitness/workouts" class="btn-primary">Vedi Allenamenti</a>
    </div>
    """

    sub_nav = [
        {'url': '/fitness', 'label': 'Home', 'icon': '🏠', 'active': True},
        {'url': '/fitness/workouts', 'label': 'Allenamenti', 'icon': '💪', 'active': False},
        {'url': '/fitness/progress', 'label': 'Progressi', 'icon': '📈', 'active': False},
    ]

    from web.templates.base import get_base_template
    return get_base_template("Salute Fisica", content, "fitness", sub_nav)