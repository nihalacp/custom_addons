{
    'name': 'Email Template',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['mail','base','sale'],
    'data': [
        "data/email_template.xml",
        "data/ir_cron_data.xml",
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}