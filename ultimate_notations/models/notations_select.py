# -*- coding: utf-8 -*-
""" Notations Select """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class NotationsSelection(models.Model):
    """ Notations Selection """
    _name = 'notations.selection'
    _order = 'category_notes'

    _sql_constraints = [
        ('code_description', 'unique (code_description)', 'A code description can be imported only once !')]

    reasons_id = fields.Many2one('notations.relations')
    code_description = fields.Char()
    category_notes = fields.Selection([('1', 'اسباب توقف الالات'),
                                       ('2', 'اسباب توقف العمال'),
                                       ('3', 'اسباب التالف')])

    notations_line_ids = fields.One2many('notations.line', 'notation_select_id')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Block'),
                              ('open', 'Open')], default='draft')
    calculation_fi = fields.Integer()

    @api.multi
    def confirm_notation(self):
        for rec in self:
            rec.write({'state': 'confirm'})
            delta = self.env['notations.line'].search([('category_notes', '=', rec.category_notes)])
            ss = len(delta)
            rec.calculation_fi = ss
            for line in delta:
                line.category_notes = rec.category_notes
                rec.notations_line_ids = line.ids

    @api.onchange('notations_line_ids')
    def change_sequence_number(self):
        for rec in self:
            for res in self.notations_line_ids:
                if res.sequence_auto == 0 and res.auto_select == True:
                    rec.calculation_fi = rec.calculation_fi + 1
                    res.sequence_auto = rec.calculation_fi
                else:
                    pass

    @api.onchange('category_notes','notations_line_ids')
    def changes_valuess(self):
        for res in self:
            for rec in res.notations_line_ids:
                rec.category_notes = res.category_notes

    @api.multi
    def cancel_notation(self):
        for rec in self:
            rec.write({'state': 'open'})
            rec.update({'notations_line_ids': None})


















