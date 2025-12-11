from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(
        selection_add=[('acopio', 'Acopio')],
        ondelete={'acopio': 'set draft'}
    )

    def action_open_acopio_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Acopio'),
            'res_model': 'acopio.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id}
        }
