# -*- coding: utf-8 -*-
{
    'name': "venta",

    'summary': """Módulo de ventas desarrollado para el proyecto de WEB2""",

    'description': """Permite visualizar todas las salidas de un negocio tipo minimarket""",

    'author': "Sebastián",
    'website': "www.utalca.cl",

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
        'views/views_boleta.xml',
        'views/views_clientes.xml',

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    # 'demo/demo.xml',
    # ],
}
