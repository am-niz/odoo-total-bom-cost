from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    total_bom_cost = fields.Float(string="Cost Price (As Per BOM)", compute="_compute_total_bom_cost", store=True)

    @api.depends('bom_ids.total_bom_cost')
    def _compute_total_bom_cost(self):
        for product in self:
            bom = self.env['mrp.bom'].search([
                ('product_tmpl_id', '=', product.id)
            ], limit=1, order='sequence, id')
            product.total_bom_cost = bom.total_bom_cost if bom else 0.0

