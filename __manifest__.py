# -*- coding: utf-8 -*-

{
    'name': "CRM Dashboard",
    'description': """CRM Dashboard""",
    'summary': """CRM dashboard module brings a multipurpose graphical dashboard"""
               """ for CRM module and making the relationship management better and easier""",
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'author': 'R',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'crm', 'sale_management'],
    'data': [
        'views/dashboard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/css/dashboard.css',
            'crm_dashboard/static/src/css/style.scss',
            'crm_dashboard/static/src/js/dashboard_view.js',

        ],
        'web.assets_qweb': [
            'crm_dashboard/static/src/xml/dashboard_view.xml',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
