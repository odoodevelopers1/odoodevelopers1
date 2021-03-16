# -*- coding: utf-8 -*-
""" Master Settings """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError


class MasterSettings(models.Model):
    """ Master Settings """
    _name = 'master.settings'
    _description = 'Master Settings'

    name = fields.Char()


