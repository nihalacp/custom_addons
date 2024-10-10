{
    'name': 'Sale Sql View',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale'],
    'data': [ 
        'security/ir.model.access.csv',
        'reports/html_report.xml',
        'views/sql_views.xml', 
        'views/print_views.xml', 
        'views/menu.xml', 
    ],
    'installable': True,
    'auto_install': False,
}