from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # Solo usar secuencia distinta si se crea desde la web
        if vals.get('website_id') and vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.web') or '/'
        return super(SaleOrder, self).create(vals)
