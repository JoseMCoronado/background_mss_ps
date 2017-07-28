# -*- coding: utf-8 -*-
{
    'name': u'Motiv Background & CSS Changes',
    'version': '1.0',
    'category': 'base',
    'description': u"""
UI Changes
""",
    'author': u'Odoo',
    'depends': [
        u'base',
    ],
    'data': [
        'data/ir_ui_view.xml',
    ],
    'static':[
        'static/src/img/motivlogo.jpg',
        'static/src/less/app_switcher2.less',
        'static/src/less/variables2.less',
        'data/ir_ui_view.xml',
    ],
    'application': True,
    'installable': True,

}
