"""
Centralized color management for the application
"""

# Color palette for different sections
COLOR_PALETTE = {
    'primary': '#4F46E5',    # Indigo
    'secondary': '#6B7280',  # Gray
    'success': '#10B981',    # Emerald
    'warning': '#F59E0B',    # Amber
    'danger': '#EF4444',     # Red
    'info': '#3B82F6',       # Blue
    'light': '#F3F4F6',      # Lighter Gray
    'dark': '#1F2937'       # Dark Gray
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
