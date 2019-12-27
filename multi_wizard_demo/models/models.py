# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DemoMultiStepWizard(models.TransientModel):
    _name = 'demo.multi.step.wizard'
    _inherit = ['multi.step.wizard.mixin']
    _description = 'Multi Step Wizard Demo'

    step1 = fields.Char('Step 1')
    step2 = fields.Char('Step 2')
    step3 = fields.Char('Step 3')

    @api.model
    def _selection_state(self):
        return [
            ('start', 'Start'),
            ('step2', 'Step 2'),
            ('step3', 'Step 3'),
            ('final', 'Final'),
        ]

    def state_exit_start(self):
        self.state = 'step2'

    def state_exit_step2(self):
        self.state = 'step3'

    def state_exit_step3(self):
        self.state = 'final'
