# -*- coding: utf-8 -*-
""" Work Centers """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class MaintenanceEquipment(models.Model):
    """ inherit Maintenance Equipment """
    _inherit = 'maintenance.equipment'

    code = fields.Char(default=lambda self:('New'),readonly=1)
    numbers_of_workers = fields.Integer(string="No Workers")
    range_price_workers = fields.Float(string="worker price average")
    type_active = fields.Selection([('active', 'Active'), ('notactive', 'Not Active')])
    machine_custom_id = fields.Many2one('mrp.workcenter')
    cost_hour = fields.Float(string="Cost/Hour")
    count = fields.Integer(default=1)

    @api.model
    def create(self, vals):
        if vals.get('code', ('New')) == ('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('maintenance.equipment') or ('New')
            delta = super(MaintenanceEquipment, self).create(vals)
            return delta


class MrpWorkcenter(models.Model):
    """ inherit Mrp Workcenter """
    _inherit = 'mrp.workcenter'

    code = fields.Char(default=lambda self:('New'),readonly=1)
    numbers_of_workers = fields.Integer(string="No Workers",compute="calculation_avrage_workers")
    range_price_workers = fields.Float(string="worker price average", compute="calculation_price_avrage")
    type_active = fields.Selection([('active', 'Active'), ('notactive', 'Not Active')])
    # equipment_ids = fields.One2many('maintenance.equipment', 'category_id', string='Equipments', copy=False)
    machine_ids = fields.One2many('maintenance.equipment', 'machine_custom_id',)
    total_workers = fields.Integer(compute="calculations_total_workers")
    count_machine = fields.Integer(compute="calculation_count_machine")
    count_price_workers = fields.Float(compute="compute_calculation_total")

    @api.depends('machine_ids')
    def calculations_total_workers(self):
        total = 0
        for rec in self.machine_ids:
            total += rec.numbers_of_workers
            self.total_workers = total

    @api.depends('machine_ids')
    def calculation_count_machine(self):
        total = 0
        for rec in self.machine_ids:
            total += rec.count
            self.count_machine = total

    @api.depends('machine_ids')
    def compute_calculation_total(self):
        total = 0
        for rec in self.machine_ids:
            total += rec.range_price_workers
            self.count_price_workers = total

    @api.depends('count_machine')
    def calculation_avrage_workers(self):
        for rec in self:
            if rec.count_machine != 0:
                rec.numbers_of_workers = rec.total_workers / rec.count_machine
            else:
                pass


    @api.depends('count_machine')
    def calculation_price_avrage(self):
        for rec in self:
            if rec.count_machine != 0:
               rec.range_price_workers = rec.count_price_workers / rec.count_machine
            else:
                pass

    # @api.constrains('numbers_of_workers')
    # def check_valedation(self):
    #     for rec in self:
    #         if rec.total_workers > rec.numbers_of_workers:
    #             raise ValidationError("error workers must be equal workers")
    @api.multi
    @api.onchange('machine_ids')
    def change_value_machine(self):
        for rec in self:
            rec.update({'equipment_ids': rec.machine_ids.ids})
            # rec.update({'machine_ids': rec.equipment_ids.ids})


    @api.model
    def create(self, vals):
        if vals.get('code', ('New')) == ('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('mrp.workcenter') or ('New')
            delta = super(MrpWorkcenter, self).create(vals)
        return delta