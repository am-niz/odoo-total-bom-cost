from odoo import fields, models, api


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    cost = fields.Float(string="Cost", related="product_id.product_tmpl_id.standard_price")
    total_cost = fields.Float(string="Total Cost", compute="_compute_total_cost")

    @api.depends("cost", "product_qty")
    def _compute_total_cost(self):
        for line in self:
            line.total_cost = line.product_qty * line.cost
