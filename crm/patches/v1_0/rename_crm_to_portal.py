import frappe

def execute():
    # Đổi tên các DocType
    rename_doctypes = [
        ("CRM Lead", "Portal Lead"),
        ("CRM Deal", "Portal Deal"),
        ("CRM Note", "Portal Note"),
        ("CRM Task", "Portal Task"),
        ("CRM Call Log", "Portal Call Log"),
        ("CRM Fields Layout", "Portal Fields Layout"),
        ("CRM Twilio Settings", "Portal Twilio Settings"),
        ("CRM Exotel Settings", "Portal Exotel Settings"),
        ("CRM Telephony Agent", "Portal Telephony Agent"),
        ("FCRM Settings", "Portal Settings"),
        ("FCRM Note", "Portal Note")
    ]

    for old_name, new_name in rename_doctypes:
        if frappe.db.exists("DocType", old_name):
            frappe.rename_doc("DocType", old_name, new_name, force=1)
            frappe.reload_doctype(new_name, force=1)

    # Đổi tên các bảng trong database
    rename_tables = [
        ("tabCRM Lead", "tabPortal Lead"),
        ("tabCRM Deal", "tabPortal Deal"),
        ("tabCRM Note", "tabPortal Note"),
        ("tabCRM Task", "tabPortal Task"),
        ("tabCRM Call Log", "tabPortal Call Log"),
        ("tabCRM Fields Layout", "tabPortal Fields Layout"),
        ("tabCRM Twilio Settings", "tabPortal Twilio Settings"),
        ("tabCRM Exotel Settings", "tabPortal Exotel Settings"),
        ("tabCRM Telephony Agent", "tabPortal Telephony Agent"),
        ("tabFCRM Settings", "tabPortal Settings"),
        ("tabFCRM Note", "tabPortal Note")
    ]

    for old_table, new_table in rename_tables:
        if frappe.db.exists("Table", old_table):
            frappe.db.sql(f"RENAME TABLE `{old_table}` TO `{new_table}`") 