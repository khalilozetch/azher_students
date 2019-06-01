# -*- coding: utf-8 -*-
from odoo import http

# class First(http.Controller):
#     @http.route('/azher_student/azher_student/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azher_student/azher_student/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('azher_student.listing', {
#             'root': '/azher_student/azher_student',
#             'objects': http.request.env['azher_student.azher_student'].search([]),
#         })

#     @http.route('/azher_student/azher_student/objects/<model("azher_student.azher_student"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azher_student.object', {
#             'object': obj
#         })