"""
Centralized color management for the application
"""

# Color palette for different sections
COLOR_PALETTE = {
    'primary': '#6366F1',    # A vibrant Indigo
    'secondary': '#64748B',  # Cool Slate Gray
    'success': '#22C55E',    # Bright Green
    'warning': '#F97316',    # Rich Orange
    'danger': '#EF4444',     # Strong Red
    'info': '#38BDF8',       # Clear Sky Blue
    'light': '#F8FAFC',      # Very Light Slate for backgrounds
    'dark': '#1E293B'       # Deep Slate for text
}

# Premium Emerald & White Theme
PREMIUM_THEME = {
    'emerald': '#10B981',        # Smeraldo vibrante
    'emerald_light': '#34D399',  # Smeraldo chiaro
    'emerald_dark': '#047857',   # Smeraldo scuro
    'white': '#FFFFFF',          # Bianco puro
    'white_light': '#F8FAFC',    # Bianco leggermente caldo
    'white_lighter': '#F1F5F9',  # Bianco ancora più chiaro
    'gold': '#FBBF24',           # Oro più caldo e moderno
    'charcoal': '#374151',       # Grigio antracite per il testo
}

# Aliases for cleaner usage in templates
BG_DARK = PREMIUM_THEME['white_light']
GOLD = PREMIUM_THEME['gold']
GOLD_LIGHT = PREMIUM_THEME['emerald_light']
GOLD_DARK = PREMIUM_THEME['emerald_dark']
BG_LIGHT = PREMIUM_THEME['white']
BG_LIGHTER = PREMIUM_THEME['white_lighter']
TEXT = PREMIUM_THEME['charcoal']
EMERALD = PREMIUM_THEME['emerald']
EMERALD_LIGHT = PREMIUM_THEME['emerald_light']
EMERALD_DARK = PREMIUM_THEME['emerald_dark']

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
