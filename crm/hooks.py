app_name = "portal_v1"
app_title = "FPT Portal"
app_publisher = "FPT"
app_description = "FPT Portal Application"
app_email = "your.email@fpt.com.vn"
app_license = "AGPLv3"
app_icon_url = "/assets/portal_v1/images/logo.svg"
app_icon_title = "Portal"
app_icon_route = "/portal"

# Apps
add_to_apps_screen = [
    {
        "name": "portal_v1",
        "logo": "/assets/portal_v1/images/logo.svg",
        "title": "FPT Portal",
        "route": "/portal",
        "has_permission": "portal_v1.api.check_app_permission",
    }
]

website_route_rules = [
    {"from_route": "/portal/<path:app_path>", "to_route": "portal"},
]

# Document Events
doc_events = {
    "Contact": {
        "validate": ["portal_v1.api.contact.validate"],
    },
    "ToDo": {
        "after_insert": ["portal_v1.api.todo.after_insert"],
        "on_update": ["portal_v1.api.todo.on_update"],
    },
    "Comment": {
        "on_update": ["portal_v1.api.comment.on_update"],
    },
    "WhatsApp Message": {
        "validate": ["portal_v1.api.whatsapp.validate"],
        "on_update": ["portal_v1.api.whatsapp.on_update"],
    },
    "Portal Deal": {
        "on_update": [
            "portal_v1.fportal.doctype.erpnext_portal_settings.erpnext_portal_settings.create_customer_in_erpnext"
        ],
    },
    "User": {
        "before_validate": ["portal_v1.api.demo.validate_user"],
        "validate_reset_password": ["portal_v1.api.demo.validate_reset_password"],
    },
}

override_doctype_class = {
    "Contact": "portal_v1.overrides.contact.CustomContact",
    "Email Template": "portal_v1.overrides.email_template.CustomEmailTemplate",
}