# -*- coding: utf-8 -*-
""" Routings """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError

class MrpRouting(models.Model):
    """ inherit Mrp Routing """
    _inherit = 'mrp.routing'

    selection_type = fields.Selection([('mix', ' وجود تداخل'), ('notmix', 'عدم وجود تداخل')])
