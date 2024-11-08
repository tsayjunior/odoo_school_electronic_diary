# -*- coding: utf-8 -*-
{
    'name': "agenda escolar academica",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assign_schedules.xml',
        'views/assign_subject.xml',
        'views/level.xml',
        'views/turn.xml',
        'views/subject.xml',
        'views/day.xml',
        'views/course.xml',
        'views/schedules.xml',
        # 'views/student.xml',
        'views/teacher.xml',
        'views/menu_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

