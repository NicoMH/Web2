# -*- coding: utf-8 -*-
{
    'name': "compra",

    'summary': """
        Desarrollo de Proyecto del módilo desarrollo web II en Odoo""",

    'description': """
        Módulo de Compra 
    """,

    'author': "David",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'inventario'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_compras.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}