# -*- coding: utf-8 -*-
""" Setting """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class ManageAttendance(models.TransientModel):
    _inherit = 'res.config.settings'

    work_hour = fields.Float(string="Fixed working hours")
    connect_with_hr = fields.Boolean(string="Linking with human resources")
    product_scrap_stock = fields.Boolean(string="Supplying combination products to the store")

    type_cost_recipt = fields.Selection([('normative', 'معياري'), ('actual', 'فعلى')],string="Type of cost on delivery")
    account_manufacture = fields.Many2one('account.account', string="Calculation of raw materials and materials in progress",config_parameter='account_manufacture')
    account_production = fields.Many2one('account.account', string="Calculation of production in progress",config_parameter='account_production')
    account_costing = fields.Many2one('account.account', string="Calculating the cost variances",config_parameter='account_costing')
    calculation_cost_not_direct = fields.Selection([('cost_hour', 'التكلفة بالساعة لمراكز التشغيل'),
                                                    ('cost_product', 'التكلفة بالحبة للمنتجات')],string="Method of calculating indirect costs")
    change_cost_range_product = fields.Float(string="Permissible percentage change in the cost of the product",default=10.0)

    def set_values(self):
        res = super(ManageAttendance, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('master_settings.work_hour', self.work_hour)
        self.env['ir.config_parameter'].sudo().set_param('master_settings.connect_with_hr', self.connect_with_hr)
        self.env['ir.config_parameter'].sudo().set_param('master_settings.product_scrap_stock', self.product_scrap_stock)
        self.env['ir.config_parameter'].sudo().set_param('master_settings.type_cost_recipt', self.type_cost_recipt)
        self.env['ir.config_parameter'].sudo().set_param('master_settings.calculation_cost_not_direct', self.calculation_cost_not_direct)
        # self.env['ir.config_parameter'].sudo().set_param('master_settings.change_cost_range_product', self.change_cost_range_product)
        return res

    @api.model
    def get_values(self):
        res = super(ManageAttendance, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        samer = ICPSudo.get_param('master_settings.work_hour', self.work_hour)
        same1 = ICPSudo.get_param('master_settings.connect_with_hr', self.connect_with_hr)
        same2 = ICPSudo.get_param('master_settings.product_scrap_stock', self.product_scrap_stock)
        same3 = ICPSudo.get_param('master_settings.type_cost_recipt', self.type_cost_recipt)
        same7 = ICPSudo.get_param('master_settings.calculation_cost_not_direct', self.calculation_cost_not_direct)
        same8 = ICPSudo.get_param('master_settings.change_cost_range_product', self.change_cost_range_product)
        res.update(work_hour=samer)
        res.update(connect_with_hr=same1)
        res.update(product_scrap_stock=same2)
        res.update(type_cost_recipt=same3)
        res.update(calculation_cost_not_direct=same7)
        # res.update(change_cost_range_product=same8)

        return res



