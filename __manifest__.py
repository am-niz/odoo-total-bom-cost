# -*- coding: utf-8 -*-
{
    'name': "total_bom_cost",

    'summary': "BOM Product Cost Price",

    'description': """
This module enables you to view the BOM cost price on both the Product and Product Template forms for products with a BOM. It also displays the total cost on the BOM form and shows the total BOM cost in both the list and kanban views of bill of matirials.    
""",

    'author': "Amzsys",
    'website': "http://www.amzsys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_bom_views.xml',
        'views/mrp_bom_line_views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
    ],
}

