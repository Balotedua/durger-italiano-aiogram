def generate_workouts_page():
    """Pagina Allenamenti"""
    content = """
    <div class="page-header">
        <h1>💪 Allenamenti</h1>
        <p>La tua routine di esercizi</p>
    </div>

    <div class="card">
        <h3>Allenamenti della Settimana</h3>
        <ul>
            <li>Lunedì: Cardio</li>
            <li>Martedì: Forza</li>
            <li>Giovedì: Flessibilità</li>
        </ul>
    </div>
    """
    
    sub_nav = [
        {'url': '/fitness', 'label': 'Home', 'icon': '🏠', 'active': False},
        {'url': '/fitness/workouts', 'label': 'Allenamenti', 'icon': '💪', 'active': True},
        {'url': '/fitness/progress', 'label': 'Progressi', 'icon': '📈', 'active': False},
    ]
    
    from web.templates.base import get_base_template
    return get_base_template("Allenamenti", content, "fitness", sub_nav)