# -*- coding: utf-8 -*-
# from odoo import http


# class OdooAlumno(http.Controller):
#     @http.route('/odoo_alumno/odoo_alumno/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_alumno/odoo_alumno/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_alumno.listing', {
#             'root': '/odoo_alumno/odoo_alumno',
#             'objects': http.request.env['odoo_alumno.odoo_alumno'].search([]),
#         })

#     @http.route('/odoo_alumno/odoo_alumno/objects/<model("odoo_alumno.odoo_alumno"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_alumno.object', {
#             'object': obj
#         })
