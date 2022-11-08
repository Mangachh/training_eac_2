# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
import base64
import random as rd
import math

class Catalogue(models.Model):
    _name = 'training.catalogue'
    _description = 'The catalogue class'

    name = fields.Char(string="Course\'s name", required=True)
    description = fields.Text(string="Course description", required=True)
    no_hours = fields.Integer(string="Number of hours", required=True)
    is_active = fields.Boolean(string="Is the course active?", default=True)

    # TODO: check if database contains name!!!
    
    def change_is_active(self) -> None:
        for rec in self:
            rec.is_active = not rec.is_active
            

class FormativeAction(models.Model):
    _name = 'training.formative_action'
    _description = 'training.formative_action'

    course_id = fields.Many2one(comodel_name='training.catalogue', string='Course',
                                required=True)
    start_date = fields.Date(string="Start date", required=True)
    participants = fields.Many2many(comodel_name='hr.employee',
    				   string='Participants')
    trainer_id = fields.Many2one(comodel_name='res.partner', string="Trainee")
    session_time = fields.Integer(string="Session time")

    # estos dos son calculados
    no_hours = fields.Integer(string="Total Course Hours",
    			     compute='_calculate_no_hours')
    no_sessions = fields.Char(string="Number of sessions",
    			     compute='_calculate_no_sessions')

    
    @api.onchange('session_time')
    def _calculate_no_sessions(self) -> None:
        for record in self:
            if record.session_time > 0:
                record.no_sessions = math.ceil(record.no_hours /
                			     record.session_time)
            else:
                record.no_sessions = 0


    @api.onchange('course_id')
    def _calculate_no_hours(self) -> None:
        for record in self:
            record.no_hours = record.course_id.no_hours
            
    
