# -*- coding: utf-8 -*-
""" Stocking Bom """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError

class ProductTemplate(models.Model):
    """ inherit Product Template """
    _inherit = 'product.template'

    volume_custom = fields.Float(compute="_related_volume_for_product")
    cost_custom = fields.Float(compute="_related_volume_for_product")

    @api.depends('volume', 'standard_price')
    def _related_volume_for_product(self):
        for rec in self:
            rec.volume_custom = rec.volume
            rec.cost_custom = rec.standard_price


class ProductTemplate(models.Model):
    """ inherit Product Template """
    _inherit = 'product.template'

    product_code = fields.Char(default=lambda self: ('New'), readonly=1)
    check_product_manufacture = fields.Boolean()
    types_production = fields.Selection([('finish', 'Finish Product'),
                                         ('half', 'Half Manufacture'),
                                         ('return', 'Return Manufacture'),
                                         ('tscrap', 'Temporary Scrap'),
                                         ('fscrap', 'Final Scrap'),
                                         ('spoiled', 'Spoiled')])
    stock_warehouse_id = fields.Many2one('stock.warehouse',string="Warehouse")

    @api.model
    def create(self, vals):
        if vals.get('product_code', ('New')) == ('New'):
            vals['product_code'] = self.env['ir.sequence'].next_by_code(
                'product.template') or ('New')
            delta = super(ProductTemplate, self).create(vals)
        return delta


class MrpBom(models.Model):
    """ inherit Mrp Bom """
    _inherit = 'mrp.bom'

    def _default_head_branch(self):
        return self.env['stock.picking.type'].search([('name', '=', 'Receipts')], limit=1).id

    bom_code = fields.Char(default=lambda self: ('New'), readonly=1)
    product_code = fields.Char(related='product_tmpl_id.product_code')
    bom_default = fields.Boolean(default=False)
    state = fields.Selection([('active', 'Active'), ('notactive', 'Not Active')])
    stock_id = fields.Many2one('stock.picking.type',index=True, ondelete='cascade',default=_default_head_branch,domain=[('name','=','Receipts')])
    product_tmpl_id = fields.Many2one('product.template',domain=[('check_product_manufacture','=', True)])
    details = fields.Binary()
    information = fields.Html()
    other = fields.Text()
    image = fields.Binary(related="product_tmpl_id.image_medium", string="Image")

    @api.onchange('product_tmpl_id')
    def auto_default_check(self):
        for rec in self:
            delta = self.env['mrp.bom'].search([('product_tmpl_id','=', rec.product_tmpl_id.id)])
            print(delta)
            if delta:
                rec.bom_default = False
            else:
                rec.bom_default = True


    @api.model
    def create(self, vals):
        if vals.get('bom_code', ('New')) == ('New'):
            vals['bom_code'] = self.env['ir.sequence'].next_by_code(
                'mrp.bom') or ('New')
            delta = super(MrpBom, self).create(vals)
        return delta


class MrpBomLine(models.Model):
    """ inherit Mrp Bom Line """
    _inherit = 'mrp.bom.line'

    quantity_line_bom = fields.Float(string="Quantity",compute="calculation_total_of_qty")
    scrap_modelas = fields.Float(string="Scrap %",compute="calculation_mdelass_scrap")
    scrap_qty = fields.Float(string="Scrap Quantity")
    warehouse_item = fields.Many2one(related='product_id.stock_warehouse_id')
    code = fields.Char(related="product_id.product_code")
    types_production = fields.Selection([('finish', 'Finish Product'),
                                         ('half', 'Half Manufacture'),
                                         ('return', 'Return Manufacture'),
                                         ('tscrap', 'Temporary Scrap'),
                                         ('fscrap', 'Final Scrap'),
                                         ('spoiled', 'Spoiled')],related="product_id.types_production")

    @api.depends('product_qty', 'scrap_qty')
    def calculation_total_of_qty(self):
        for rec in self:
            rec.quantity_line_bom = rec.product_qty + rec.scrap_qty

    @api.depends('scrap_qty','product_qty')
    def calculation_mdelass_scrap(self):
        for rec in self:
            delta =  rec.scrap_qty / rec.product_qty *100
            rec.scrap_modelas = delta