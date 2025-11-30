"""
Centralized color management for the application with a premium, modern palette.
"""

# Premium & Modern Color Palette
# Designed for elegance, high contrast, and a contemporary feel.
# Primarily optimized for a dark theme, but easily adaptable for light mode.
THEME_COLORS = {
    # --- Backgrounds (Dark Shades for Depth) ---
    'bg_dark_900': '#1A1A2E',  # Deep Indigo/Navy - Primary background
    'bg_dark_800': '#232946',  # Dark Blue-Gray - Secondary background (cards, sections)
    'bg_dark_700': '#2E3250',  # Medium Blue-Gray - Tertiary background (input fields, hover states)
    'bg_dark_600': '#41476B', # Slightly lighter for subtle variations

    # --- Text Colors (High Readability) ---
    'text_light_100': '#E0E0E0',  # Off-White - Primary text
    'text_light_200': '#A0A0B0',  # Light Gray - Secondary text, muted info
    'text_light_300': '#7D7D9A',  # Muted Gray - Tertiary text, placeholders

    # --- Primary Accent (Vibrant & Distinct) ---
    'accent_primary_500': '#BB2649', # Rich Rose/Berry - Main interactive element color
    'accent_primary_400': '#D43C60', # Lighter accent for hover/active states
    'accent_primary_600': '#A51F3D', # Darker accent for pressed/stronger emphasis

    # --- Secondary & Status Accents ---
    'accent_secondary_500': '#6B5B95', # Muted Violet - Secondary interactive element, subtle emphasis
    'accent_success': '#28B463', # Emerald Green - Success messages, positive indicators
    'accent_danger': '#E74C3C',  # Vibrant Red - Error messages, warnings
    'accent_warning': '#F4D03F', # Golden Yellow - Warnings, important alerts
    'accent_info': '#3498DB',    # Bright Blue - Informational messages, highlights

    # --- Borders & Dividers ---
    'border_dark': '#3A3F5B',    # Dark Gray-Blue - Subtle separators
    'border_light': '#555A7B',   # Lighter Gray-Blue - Stronger separators
}

# Aliases for easier access and common usage across the application
# Backgrounds
BG_MAIN = THEME_COLORS['bg_dark_900']
BG_CARD = THEME_COLORS['bg_dark_800']
BG_SECONDARY = THEME_COLORS['bg_dark_700']
BG_INPUT = THEME_COLORS['bg_dark_700'] # Often same as secondary

# Text
TEXT_PRIMARY = THEME_COLORS['text_light_100']
TEXT_SECONDARY = THEME_COLORS['text_light_200']
TEXT_MUTED = THEME_COLORS['text_light_300']

# Accents
PRIMARY_ACCENT = THEME_COLORS['accent_primary_500']
PRIMARY_ACCENT_LIGHT = THEME_COLORS['accent_primary_400']
PRIMARY_ACCENT_DARK = THEME_COLORS['accent_primary_600']

SECONDARY_ACCENT = THEME_COLORS['accent_secondary_500']

SUCCESS = THEME_COLORS['accent_success']
DANGER = THEME_COLORS['accent_danger']
WARNING = THEME_COLORS['accent_warning']
INFO = THEME_COLORS['accent_info']

BORDER_DEFAULT = THEME_COLORS['border_dark']

# Module-specific colors (using new palette)
MODULE_COLORS = {
    'home': PRIMARY_ACCENT,
    'finance': SUCCESS,
    'psychology': SECONDARY_ACCENT,
    'fitness': DANGER,
    'durger_king': WARNING,
    'dashboard': INFO,
    'badge': WARNING,
    'career': PRIMARY_ACCENT,
    'mental_health': SECONDARY_ACCENT,
    'detox': SUCCESS,
    'time_management': INFO,
    'news': WARNING,
    'notes': BG_DARK_700 # Example: using a background color for a module accent
}

def get_module_color(module_name: str) -> str:
    """Get color for a specific module."""
    return MODULE_COLORS.get(module_name, PRIMARY_ACCENT)

def get_theme_colors() -> dict:
    """Get the complete theme color palette."""
    return THEME_COLORS

def update_module_color(module_name: str, color: str):
    """Update color for a specific module."""
    MODULE_COLORS[module_name] = color

def get_css_variables() -> str:
    """Generate CSS variables for the theme color palette."""
    css_vars = []
    for name, color in THEME_COLORS.items():
        css_vars.append(f'--color-{name.replace("_", "-")}: {color};')
    return '\n'.join(css_vars)

