# -*- coding: utf-8 -*-
{
    'name': "待办事项",

    'summary': "待办事项",

    'description': "待办事项",

    'author': "Ruter",
    'website': "https://ruterly.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/todo_security.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/views.xml',
        'views/templates.xml',
	    'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
