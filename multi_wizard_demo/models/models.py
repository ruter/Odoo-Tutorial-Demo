# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.TransientModel):
    _name = 'demo.multi.step.wizard'
    _inherit = ['multi.step.wizard.mixin']
    _description = 'Multi Step Wizard Demo'
