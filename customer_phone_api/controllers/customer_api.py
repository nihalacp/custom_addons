from odoo import http
from odoo.http import request
import json


class CustomerAPIController(http.Controller):

    @http.route('/get_customer', type='http', auth='public', methods=['POST'], csrf=False)
    def get_customer_details(self, **data_passed):
        kwargs = request.get_json_data()
        phone = kwargs.get('phone')
        if not phone:
            return {'error': 'Phone number is required'}

        customer = request.env['res.partner'].sudo().search([('phone', '=', phone)], limit=1)

        if not customer:
            return {'error': 'Customer not found'}
        data = {
            'name': customer.name,
            'address': customer.city,
            'street': customer.street,
            'city': customer.city,
            'country_id': customer.country_id.name,
        }
        return request.make_response(http.json.dumps(data),
            headers={'Content-Type': 'application/json'})
    


class CustomerAPIControllerPhone(http.Controller):
          @http.route('/api/get_partner_by_phone', type='http', auth='public', methods=['GET'], csrf=False)
          def get_partner_by_phone(self, **kwargs):
                    phone = kwargs.get('phone')
                    if not phone:
                              return request.make_response("Phone number is required", headers={'Content-Type': 'application/json'}, status=400)
                    
                    partner = request.env['res.partner'].sudo().search([('phone', '=', phone)], limit=1)
                    
                    if not partner:
                              return request.make_response("Partner not found", headers={'Content-Type': 'application/json'}, status=404)
                    
                    partner_data = {
                              'id': partner.id,
                              'name': partner.name,
                              'email': partner.email,
                              'phone': partner.phone,
                              'company_name': partner.company_name,
                              'street': partner.street,
                              'city': partner.city,
                              'country_id': partner.country_id.name,
                              'vat': partner.vat,
                              'website': partner.website,
                    }
                    return request.make_response(
                              http.json.dumps(partner_data),
                              headers={'Content-Type': 'application/json'}
                    )
