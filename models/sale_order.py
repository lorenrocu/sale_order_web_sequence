from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # Solo usar secuencia distinta si se crea desde la web y no es una transacción de pago
        # Evitar interferir con órdenes creadas por pasarelas de pago
        if (vals.get('website_id') and 
            vals.get('name', '/') == '/' and 
            not vals.get('transaction_ids') and  # No es una transacción de pago
            not self.env.context.get('payment_processing')):  # No está en proceso de pago
            
            try:
                sequence = self.env['ir.sequence'].next_by_code('sale.order.web')
                if sequence:
                    vals['name'] = sequence
                    _logger.info('Asignada secuencia web: %s', sequence)
                else:
                    _logger.warning('No se pudo obtener secuencia sale.order.web, usando secuencia por defecto')
            except Exception as e:
                _logger.error('Error al obtener secuencia web: %s', str(e))
                # En caso de error, continuar con el flujo normal
                
        return super(SaleOrder, self).create(vals)
