{
    'name': 'Sale Order Excel',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/excel_report_views.xml',
        'reports/report.xml',
        'reports/template_html.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}