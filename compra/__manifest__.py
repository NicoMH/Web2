# -*- coding: utf-8 -*-
{
    'name': "Compra",

    'summary': """
        Desarrollo del proyecto de Desarrollo de aplicacines web 2, modulo Compra en Odoo""",

    'description': """
        Registrar los datos de los proveedores y las compras que el minimarket les realiza para abastecerse""",

    'author': "David Mora",
    'website': "http://www.yourcompany.com",

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
        'views/views_proveedor.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
        #'demo/demo.xml',
    #],
}