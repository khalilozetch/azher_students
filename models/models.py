from odoo import models ,fields
class AzherStudent(models.Model):
    _name = "azher.student"
    name = fields.Char(string="Name", required=False, )
    age = fields.Integer(string="Age", required=False, )
    salary = fields.Float(string="Salary")
    image = fields.Binary()
    is_accepted = fields.Boolean(string="Accespted")
    bio = fields.Text(string="Bio")
    cv = fields.Html(string="",  )
    grade = fields.Selection(selection=[('g', 'good'), ('vg', 'very good'), ('d', 'distinct')])
    track_id = fields.Many2one(comodel_name="azher.track", string="Track", )
    skills_ids = fields.Many2many(comodel_name="azher.skill", string="Skills", )

class AzherTrack(models.Model):
    _name = "azher.track"
    _rec_name = 'name'
    students_ids = fields.One2many(comodel_name="azher.student", inverse_name="track_id", string="Students", required=False, )
    name = fields.Char(string=" Students Name")

class AzherSkill(models.Model):
    _name = "azher.skill"
    _rec_name="skill"
    skill= fields.Char(string="Name" )