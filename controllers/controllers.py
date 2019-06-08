# -*- coding: utf-8 -*-
from odoo import http

# class First(http.Controller):
#     @http.route('/azherSstudent/azherSstudent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azherSstudent/azherSstudent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('azherSstudent.listing', {
#             'root': '/azherSstudent/azherSstudent',
#             'objects': http.request.env['azherSstudent.azherSstudent'].search([]),
#         })

#     @http.route('/azherSstudent/azherSstudent/objects/<model("azherSstudent.azherSstudent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azherSstudent.object', {
#             'object': obj
#         })