{
    'name': 'HTML Report',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/html_report_views.xml',
        'reports/html_report.xml',
        'reports/html_template.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}