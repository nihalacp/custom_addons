{
    "name": "Hospital Management System",
    "author": "nin",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    "depends": ['mail', 'product', 'report_xlsx' ], 
                
    "data": [
        "security/security.xml",
        "security/prescription_security.xml",
        # "security/hospital_access_control_security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/mail_template_data.xml",
        "data/patient_mail_template.xml",
        "wizard/create_appointment_view.xml",
        "wizard/excel_report_views.xml",
        "reports/report.xml",
        "reports/patient_template.xml",
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/appointment_line_views.xml",
        "views/patient_tag_views.xml",
        "views/prescription_views.xml",
        "views/menu.xml",
    ]
}