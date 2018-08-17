# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项'

    name = fields.Char('描述', required=True)
    is_done = fields.Boolean('已完成？')
    priority = fields.Selection([
        ('todo', '待办'),
        ('normal', '普通'),
        ('urgency', '紧急')
    ], default='todo', string='紧急程度')
    deadline = fields.Datetime(u'截止时间')
    is_expired = fields.Boolean(u'已过期', compute='_compute_is_expired')

    @api.depends('deadline')
    @api.multi
    def _compute_is_expired(self):
        for record in self:
            record.is_expired = record.deadline < fields.Datetime.now()
