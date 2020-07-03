# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Odoo Googletagmanager',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['website'],
    'data': [
        'data/ir_configparameter_data.xml',
        'views/assets.xml',                
    ],    
    'installable': True,
    'auto_install': False,    
}