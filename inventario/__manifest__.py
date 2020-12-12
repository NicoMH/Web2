# -*- coding: utf-8 -*-
{
    'name': "Inventario",

    'summary': """
        Módulo Desarrollado para el ramo de Desarrollo de Aplicaciones Web II""",

    'description': """
        Módulo creado para registrar las existencias en bodega
    """,

    'author': "Nicolás",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_inventario.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
}