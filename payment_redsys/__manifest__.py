# -*- coding: utf-8 -*-
{
    'name': 'Redsys Payment Acquirer',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['website_portal_sale'],
    'external_dependencies': {
        'python': [
            'Crypto.Cipher.DES3',
        ],
        'bin': [],
    },
    'data': [
        'views/redsys.xml',
        'views/payment_acquirer.xml',
        'data/payment_redsys.xml'
    ],
    'installable': True,
    'auto_install': False,    
}