{
    'name': 'many2one inherit',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['sale', 'om_hospital'],
    'data': [
        "security/patient_security.xml",
        "security/ir.model.access.csv",
        "views/many2one_views.xml",
    ],
    'installable': True,
    'auto_install': False,
}