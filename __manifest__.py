# -*- coding: utf-8 -*-
{
    'name': "Training",

    'summary': """
        A simple course-traing module to test custom modules on Odoo""",

    'description': """
        A module necessary to pass EAC2 from IOC's DAM-M10-S1 2022. 
        The module consist of two classes:
            - One that stores the course's information (name, description, total hours)
            - One that stores the course to do, the trainee, the employees that will attend the course,
              the start date,...        
    """,

    'author': "Lluís Cobos Aumatell",
    'website': "https://github.com/Mangachh/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Base Module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/css_loader.xml',
        'views/menus.xml'
    ],

    'installable': True,
    'application': True,
}
