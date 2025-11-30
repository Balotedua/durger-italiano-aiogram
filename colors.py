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

# Premium Emerald & White Theme - Organized by function
PREMIUM_THEME = {
    # Primary colors
    'primary': '#10B981',        # Main emerald
    'primary_light': '#34D399',  # Light emerald
    'primary_dark': '#047857',   # Dark emerald
    
    # Background colors
    'bg_main': '#F8FAFC',        # Main background
    'bg_card': '#FFFFFF',        # Card background
    'bg_light': '#F1F5F9',       # Light background
    
    # Text colors
    'text_primary': '#374151',   # Main text
    'text_secondary': '#6B7280', # Secondary text
    'text_accent': '#10B981',    # Accent text
    
    # Accent colors
    'accent_gold': '#FBBF24',    # Gold accent
    'accent_emerald': '#10B981', # Emerald accent
}

# Functional aliases for cleaner usage in templates
# Backgrounds
BG_DARK = PREMIUM_THEME['bg_main']
BG_LIGHT = PREMIUM_THEME['bg_card']
BG_LIGHTER = PREMIUM_THEME['bg_light']

# Text
TEXT = PREMIUM_THEME['text_primary']
TEXT_SECONDARY = PREMIUM_THEME['text_secondary']
TEXT_ACCENT = PREMIUM_THEME['text_accent']

# Primary colors
PRIMARY = PREMIUM_THEME['primary']
PRIMARY_LIGHT = PREMIUM_THEME['primary_light']
PRIMARY_DARK = PREMIUM_THEME['primary_dark']

# Accents
ACCENT_GOLD = PREMIUM_THEME['accent_gold']
ACCENT_EMERALD = PREMIUM_THEME['accent_emerald']

# Legacy aliases for backward compatibility
EMERALD = PREMIUM_THEME['primary']
EMERALD_LIGHT = PREMIUM_THEME['primary_light']
EMERALD_DARK = PREMIUM_THEME['primary_dark']
GOLD = PREMIUM_THEME['accent_gold']
GOLD_LIGHT = PREMIUM_THEME['primary_light']
GOLD_DARK = PREMIUM_THEME['primary_dark']

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
