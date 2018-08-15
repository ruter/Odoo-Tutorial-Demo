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
