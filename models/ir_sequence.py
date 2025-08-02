from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    @api.model
    def _create_web_sequence_if_not_exists(self, code, name, prefix, padding):
        """Crea la secuencia web solo si no existe una personalizada"""
        existing_sequence = self.search([('code', '=', code)], limit=1)
        
        if existing_sequence:
            _logger.info('Secuencia %s ya existe (ID: %s), manteniendo configuración personalizada', 
                        code, existing_sequence.id)
            return existing_sequence
        
        # Crear secuencia por defecto solo si no existe
        sequence = self.create({
            'name': name,
            'code': code,
            'prefix': prefix,
            'padding': padding,
            'company_id': False,
        })
        
        _logger.info('Creada nueva secuencia %s (ID: %s) con prefijo %s', 
                    code, sequence.id, prefix)
        return sequence