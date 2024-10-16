from odoo import http
from odoo.http import request, Response
import json

class CustomerAPIController(http.Controller):

    @http.route('/api/customers', type='http', auth='public', methods=['GET'], csrf=False)
    def get_customers(self, **kwargs):
        """Returns a list of customers with details"""
        try:
            customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
            data = []
            for customer in customers:
                data.append({
                    'id': customer.id,
                    'name': customer.name,
                    'email': customer.email,
                    'phone': customer.phone,
                    'company_name': customer.company_name,
                    'is_company': customer.is_company,
                })
            return Response(
                json.dumps({'status': 'success', 'customers': data}),
                content_type='application/json',
                status=200
            )
        except Exception as e:
            return Response(
                json.dumps({'status': 'error', 'message': str(e)}),
                content_type='application/json',
                status=500
            )



# from odoo import http
# from odoo.http import request, Response

# class CustomerAPI(http.Controller):

#     @http.route('/api/customer', type='json', auth='public', methods=['POST'], csrf=False)
#     def get_customer_by_phone(self, phone=None):
#           if not phone:
#                     return {'error': 'Phone number is required.'}

#           customer = request.env['res.partner'].sudo().search([('phone', '=', phone)], limit=1)

#           if not customer:
#                     return {'error': 'Customer not found.'}

#           return {
#                     'name': customer.name,
#                     'address': customer.contact_address,
#           }

