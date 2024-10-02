from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    total_bom_cost = fields.Float(string="Cost Price (As Per BOM)", compute="_compute_total_bom_cost", store=True)

    @api.depends('product_tmpl_id.bom_ids', 'product_tmpl_id.bom_ids.total_bom_cost')
    def _compute_total_bom_cost(self):
        for product in self:
            bom = self.env['mrp.bom'].search([
                '|',
                ('product_id', '=', product.id),
                '&',
                ('product_id', '=', False),
                ('product_tmpl_id', '=', product.product_tmpl_id.id)
            ], limit=1, order='sequence, product_id desc, id')
            product.total_bom_cost = bom.total_bom_cost if bom else 0.0
