{
    'name': 'Customer Invoice Report',
    'version': '18.0.1.0.0',
    'summary': 'Customer Invoice PDF Report',
    'description': 'Custom Customer Invoice PDF report for Odoo 18.',
    'category': 'Accounting/Localizations',
    'author': 'Saad Dar',
    'depends': ['account', 'sale'],
    'data': [
        'report/report_action.xml',
        'report/report_template.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
