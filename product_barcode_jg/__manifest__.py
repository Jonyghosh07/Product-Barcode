# -*- coding: utf-8 -*-

# Copyright © 2025 Jony Ghosh
{
    'name': "Product Auto Barcode Image Generator",

    'summary': """
        Automatically Generate Barcode Image for Product
        """,

    'description': """
        This module generates a barcode image for each product template in Odoo.
        The barcode image is stored in the 'barcode_img' field of the product template model.
        The barcode is generated using the internal reference and is displayed in the product template form view.
    """,

    'author': "Jony Ghosh",
    'maintainer': 'Jony Ghosh',
    'license': 'OPL-1',


    'category': 'Tools/Tools',
    'version': '18.0.0.1',

    'images': ['static/src/img/banner.png'],
    'icon': "/product_barcode_jg/static/src/img/icon.png",
    
    'depends': ['product', 'barcodes'],

    
    'data': [
        'views/product_view.xml',
    ],
    
    'demo': [],
    'sequence':-133,
    'price': 10.0,
    'currency':'EUR',
    'application': True,
    'installable': True,
    'auto_install': False,
}