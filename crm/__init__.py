__title__ = "Frappe Portal"
__version__ = "1.0.0"

import frappe

no_cache = 1

def get_context(context):
    context.show_sidebar = True
    context.no_cache = 1
    context.title = "Portal"
    context.breadcrumbs = [{"label": "Portal", "route": "/portal"}]
    return context

