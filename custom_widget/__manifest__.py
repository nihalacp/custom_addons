{
    'name': 'My Custom Module',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        'views/custom_model_views.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'custom_widget/static/src/js/custom_widget.js',  # Add your custom JS widget
    #         'custom_widget/static/src/css/custom_widget.css',  # Optional custom CSS
    #     ],
    # },
    'installable': True,
    'auto_install': False,
    'application': True,
}