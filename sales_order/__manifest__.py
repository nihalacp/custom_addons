{
    'name': 'Custom Sales Module',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale', 'sale_management','product', 'account'],
    'data': [
       'views/sale_order_views.xml',
       'views/sale_order_line_views.xml',
       'views/product_views.xml',
       'views/account_move_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}