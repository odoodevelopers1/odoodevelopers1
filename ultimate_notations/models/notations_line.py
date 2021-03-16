# -*- coding: utf-8 -*-
""" Notations Line """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class NotationsLine(models.Model):
    """ Notations Line """
    _name = 'notations.line'
    _description = 'Notations Line'

    name = fields.Char(string="Notations Name")
    code = fields.Char(readonly=1, string="Sequence")
    sequence_auto = fields.Integer()
    codeing_custom = fields.Integer( default=1)
    state = fields.Selection([('active', 'Active'), ('notactive', 'Not Active')],string="State")
    notation_select_id = fields.Many2one('notations.selection')
    category_notes = fields.Selection([('1', 'اسباب توقف الالات'),
                                       ('2', 'اسباب توقف العمال'),
                                       ('3', 'اسباب التالف')], string="Notes Category")
    reasons_id = fields.Many2one('notations.relations')
    new_codeing = fields.Integer(compute="calculate_depend_value")
    auto_select = fields.Boolean(string="Test", default=False, compute='change_select_auto')

    @api.depends('sequence_auto')
    def calculate_depend_value(self):
        '''this fuction to help fuction in notations select if auto_select true the line will sequence auto'''
        for rec in self:
            if rec.sequence_auto != 0:
                rec.new_codeing = rec.sequence_auto
            else:
                pass

    @api.onchange('name', 'category_notes')
    def change_select_auto(self):
        '''this fuction to help fuction in notations select if auto_select true the line will sequence auto'''
        for res in self:
            if res.name and res.category_notes != False or None or 0:
                res.auto_select = True

    @api.model
    def create(self, vals):
        '''create Sequence Automatic By odoo sequrnce'''
        vals['code'] = self.env['ir.sequence'].next_by_code('notations.line')
        delta = super(NotationsLine, self).create(vals)
        return delta




