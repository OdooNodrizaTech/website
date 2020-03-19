# -*- coding: utf-8 -*-
{
    'name': 'Website Noindex',
    'version': "10.0.1.0.0,    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['website'],
    'data': [
        'views/website-config-settings.xml',
        'templates/assets.xml',
        'templates/website_layout.xml',
        'templates/website_navbar.xml',
    ],
    'installable': True,
    'auto_install': False,    
}