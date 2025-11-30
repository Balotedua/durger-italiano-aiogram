"""
Centralized color management for the application
"""

# Color palette for different sections
COLOR_PALETTE = {
    'primary': '#4F46E5',    # A sophisticated Indigo
    'secondary': '#6B7280',  # A muted Gray
    'success': '#10B981',    # A soft Emerald Green
    'warning': '#F59E0B',    # A warm Amber
    'danger': '#EF4444',     # A classic Red
    'info': '#3B82F6',       # A vibrant Blue
    'light': '#F9FAFB',      # Very light neutral for backgrounds
    'dark': '#111827'        # Deep charcoal for text
}

# Minimal Premium Theme - High Contrast & Elegant
PREMIUM_THEME = {
    # Primary colors - Deep and rich for a professional feel
    'primary': '#1F2937',        # Dark Slate (primary brand color)
    'primary_light': '#374151',  # Medium Slate
    'primary_dark': '#111827',   # Deep Charcoal

    # Background colors - Clean and subtle
    'bg_main': '#FFFFFF',        # Pure White
    'bg_card': '#F9FAFB',        # Off-White (subtle contrast for cards)
    'bg_light': '#E5E7EB',       # Light Gray (for subtle sections/dividers)
    
    # Text colors - High contrast for readability
    'text_primary': '#1F2937',   # Dark Slate
    'text_secondary': '#6B7280', # Muted Gray
    'text_accent': '#4F46E5',    # Sophisticated Indigo (for links/highlights)
    
    # Accent colors - Elegant and purposeful
    'accent_primary': '#4F46E5', # Sophisticated Indigo (main accent)
    'accent_secondary': '#1F2937', # Dark Slate (secondary accent, cohesive)
    'border_light': '#D1D5DB',   # Light Silver (for subtle borders)
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
ACCENT_PRIMARY = PREMIUM_THEME['accent_primary']
ACCENT_SECONDARY = PREMIUM_THEME['accent_secondary']
BORDER_LIGHT = PREMIUM_THEME['border_light']

# Legacy aliases for backward compatibility
EMERALD = PREMIUM_THEME['primary']
EMERALD_LIGHT = PREMIUM_THEME['primary_light']
EMERALD_DARK = PREMIUM_THEME['primary_dark']
GOLD = PREMIUM_THEME['accent_primary']
GOLD_LIGHT = PREMIUM_THEME['primary_light']
GOLD_DARK = PREMIUM_THEME['primary_dark']
ACCENT_GOLD = PREMIUM_THEME['accent_primary']
ACCENT_EMERALD = PREMIUM_THEME['primary']

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
