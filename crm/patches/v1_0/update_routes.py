import frappe

def execute():
    # Cập nhật các route trong DocType
    update_routes = [
        ("Portal Lead", "/portal/leads"),
        ("Portal Deal", "/portal/deals"),
        ("Portal Note", "/portal/notes"),
        ("Portal Task", "/portal/tasks"),
        ("Portal Call Log", "/portal/call-logs"),
        ("Portal Fields Layout", "/portal/fields-layout"),
        ("Portal Twilio Settings", "/portal/twilio-settings"),
        ("Portal Exotel Settings", "/portal/exotel-settings"),
        ("Portal Telephony Agent", "/portal/telephony-agent"),
        ("Portal Settings", "/portal/settings")
    ]

    for doctype, route in update_routes:
        if frappe.db.exists("DocType", doctype):
            frappe.db.set_value("DocType", doctype, "route", route)

    # Cập nhật các path trong file system
    update_paths = [
        ("/crm", "/portal"),
        ("/crm/leads", "/portal/leads"),
        ("/crm/deals", "/portal/deals"),
        ("/crm/notes", "/portal/notes"),
        ("/crm/tasks", "/portal/tasks"),
        ("/crm/call-logs", "/portal/call-logs"),
        ("/crm/settings", "/portal/settings")
    ]

    for old_path, new_path in update_paths:
        frappe.db.sql(f"""
            UPDATE `tabFile`
            SET file_url = REPLACE(file_url, '{old_path}', '{new_path}')
            WHERE file_url LIKE '{old_path}%'
        """) 