# -*- coding: utf-8 -*-
{
    'name': "Database | Manager",

    'summary': """
        Database | Manager""",

    'description': """
        Database | Manager
    """,

    'author': "Daniel",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base','mail','account'],

    'data': [
        'security/ir.model.access.csv',
        'views/view_admin_manager.xml',
        'views/view_admin_server.xml',
        'views/view_admin_user.xml',
        'views/view_account_move.xml',
        'views/view_menu.xml'
    ],

}
