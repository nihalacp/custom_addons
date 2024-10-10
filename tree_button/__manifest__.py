{
    'name': 'Tree View Button',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale','web'],
    'data': [
        "security/ir.model.access.csv",
        'views/button_views.xml',
        'views/sale_compare_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tree_button/static/src/js/tree_button.js',  
            'tree_button/static/src/xml/tree_button.xml',      
        ],
    },
    'installable': True,
    'auto_install': False,
}