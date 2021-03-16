# -*- coding: utf-8 -*-
""" Notations Relations """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class NotationsRelations(models.Model):
    """ Notations Relations """
    _name = 'notations.relations'
    _description = 'Notations Relations'

    name = fields.Char()
    relations_id = fields.Many2one('notations.relations')
    category_notes = fields.Selection([('1', 'اسباب توقف الالات'),
                                       ('2', 'اسباب توقف العمال'),
                                       ('3', 'اسباب التالف')])

