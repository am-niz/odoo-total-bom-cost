from odoo import fields, models, api


class MrpBomLine(models.Model):
    _inherit = "mrp.bom"

    total_bom_cost = fields.Float(string="Total BOM Cost", compute="_compute_total_bom_cost", store=True)

    @api.depends('bom_line_ids.product_qty', 'bom_line_ids.product_id.standard_price')
    def _compute_total_bom_cost(self):
        for bom in self:
            bom.total_bom_cost = sum(line.product_qty * line.product_id.standard_price for line in bom.bom_line_ids)
