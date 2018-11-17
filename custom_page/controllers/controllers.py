# -*- coding: utf-8 -*-
from odoo import http

# class CustomPage(http.Controller):
#     @http.route('/custom_page/custom_page/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_page/custom_page/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_page.listing', {
#             'root': '/custom_page/custom_page',
#             'objects': http.request.env['custom_page.custom_page'].search([]),
#         })

#     @http.route('/custom_page/custom_page/objects/<model("custom_page.custom_page"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_page.object', {
#             'object': obj
#         })