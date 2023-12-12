# -*- coding: utf-8 -*-
# from odoo import http


# class TestAccessRights(http.Controller):
#     @http.route('/test_access_rights/test_access_rights', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_access_rights/test_access_rights/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_access_rights.listing', {
#             'root': '/test_access_rights/test_access_rights',
#             'objects': http.request.env['test_access_rights.test_access_rights'].search([]),
#         })

#     @http.route('/test_access_rights/test_access_rights/objects/<model("test_access_rights.test_access_rights"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_access_rights.object', {
#             'object': obj
#         })
