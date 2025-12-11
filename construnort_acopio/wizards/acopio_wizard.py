from odoo import models, fields, api, _


class AcopioWizard(models.TransientModel):
    _name = 'acopio.wizard'
    _description = 'Wizard para cambiar estado acopio'

    order_id = fields.Many2one('sale.order', string='Pedido de venta', required=True)
    acopio_bool = fields.Boolean(string='¿Aplicar estado Acopio?')

    def action_confirm(self):
        self.ensure_one()
        if self.acopio_bool:
            self.order_id.state = 'acopio'
        else:
            self.order_id.state = 'draft'
        return {'type': 'ir.actions.act_window_close'}
