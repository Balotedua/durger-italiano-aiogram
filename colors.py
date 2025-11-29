"""
Centralized color management for the application
"""

# Color palette for different sections
COLOR_PALETTE = {
    'primary': '#dc2626',
    'secondary': '#8b5cf6',
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
    'info': '#3b82f6',
    'light': '#f8fafc',
    'dark': '#1e293b'
}

# Module-specific colors
MODULE_COLORS = {
    'home': COLOR_PALETTE['primary'],
    'finance': COLOR_PALETTE['success'],
    'psychology': COLOR_PALETTE['secondary'],
    'fitness': COLOR_PALETTE['danger'],
    'durger_king': COLOR_PALETTE['warning'],
    'dashboard': COLOR_PALETTE['info'],
    'badge': COLOR_PALETTE['warning'],
    'career': COLOR_PALETTE['primary'],
    'mental_health': COLOR_PALETTE['secondary'],
    'detox': COLOR_PALETTE['success'],
    'time_management': COLOR_PALETTE['info'],
    'news': COLOR_PALETTE['warning'],
    'notes': COLOR_PALETTE['dark']
}

def get_module_color(module_name):
    """Get color for a specific module"""
    return MODULE_COLORS.get(module_name, COLOR_PALETTE['primary'])

def get_color_palette():
    """Get the complete color palette"""
    return COLOR_PALETTE

def update_module_color(module_name, color):
    """Update color for a specific module"""
    MODULE_COLORS[module_name] = color

def get_css_variables():
    """Generate CSS variables for the color palette"""
    css_vars = []
    for name, color in COLOR_PALETTE.items():
        css_vars.append(f'--color-{name}: {color};')
    return '\n'.join(css_vars)
