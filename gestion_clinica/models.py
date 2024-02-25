# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'clinica.paciente'
    _description = 'Modelo para gestionar pacientes'

    # Definir los campos para la gestión de pacientes
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    tipo_documento = fields.Selection([('dni', 'DNI'), ('pasaporte', 'Pasaporte'), ('otros', 'Otros')], string='Tipo de Documento', required=True)
    numero_documento = fields.Char(string='Número de Documento', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    genero = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], string='Género', required=True)
    direccion = fields.Char(string='Dirección', required=True)
    ciudad = fields.Char(string='Ciudad', required=True)
    codigo_postal = fields.Char(string='Código Postal', required=True)
    telefono = fields.Char(string='Teléfono', required=True)

    # Relación uno a muchos con acompañantes
    acompanantes_ids = fields.One2many('clinica.acompanante', 'paciente_id', string='Acompañantes')

    # Relación uno a muchos con diagnósticos médicos
    diagnosticos_ids = fields.One2many('clinica.diagnostico', 'paciente_id', string='Diagnósticos Médicos')



class Acompanante(models.Model):
    _name = 'clinica.acompanante'
    _description = 'Modelo para gestionar acompañantes'

    # Definir los campos para la gestión de acompañantes
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    parentesco = fields.Selection([('madre', 'Madre'), ('padre', 'Padre'), ('hijo', 'Hijo'), ('otro', 'Otro')], string='Parentesco', required=True)
    telefono_contacto = fields.Char(string='Teléfono de Contacto', required=True)
    paciente_id = fields.Many2one('clinica.paciente', string='Paciente')

class Diagnostico(models.Model):
    _name = 'clinica.diagnostico'
    _description = 'Modelo para gestionar diagnósticos médicos'

    # Definir los campos para la gestión de diagnósticos
    d_nomenclado_id = fields.Many2one('clinica.d_nomenclado', string='Diagnóstico', required=True)
    fecha_diagnostico = fields.Date(string='Fecha del Diagnóstico', required=True)
    medico_id = fields.Many2one('clinica.medico', string='Médico', required=True)
    paciente_id = fields.Many2one('clinica.paciente', string='Paciente') 

class DiagnosticoNomenclado(models.Model):
    _name = "clinica.d_nomenclado"
    _description = 'Modelo para gestionar nomenclaturas de diagnósticos'

    name = fields.Char(string='Diagnóstico', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    diagnostico_ids = fields.One2many('clinica.diagnostico', 'd_nomenclado_id', string='Diagnósticos')
    pacientes_ids = fields.Many2many('clinica.paciente', string='Pacientes', compute='_compute_pacientes_ids')

    @api.depends('diagnostico_ids.paciente_id')
    def _compute_pacientes_ids(self):
        for record in self:
            pacientes = record.diagnostico_ids.mapped('paciente_id')
            record.pacientes_ids = [(6, 0, pacientes.ids)]

class Medico(models.Model):
    _name = 'clinica.medico'
    _description = 'Modelo para gestionar médicos'

    # Definir los campos para la gestión de médicos

    name = fields.Char(string='Nombre', required=True)
    matricula = fields.Char(string='Matrícula', required=True)
    diagnosticos_ids = fields.One2many('clinica.diagnostico', 'medico_id', string='Diagnósticos')

