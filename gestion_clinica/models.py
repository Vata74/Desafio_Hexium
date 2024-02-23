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

    @api.model
    def buscar_pacientes_por_diagnostico(self, nombre_diagnostico):
        diagnosticos = self.env['clinica.diagnostico'].search([('nombre_diagnostico', '=', nombre_diagnostico)])
        pacientes = diagnosticos.mapped('paciente_id')
        return pacientes

    @api.model
    def crear_paciente(self, vals):
        paciente = self.create(vals)
        return paciente

    @api.model
    def asociar_diagnostico_a_paciente(self, tipo_documento, numero_documento, diagnostico_vals):
        paciente = self.search([('tipo_documento', '=', tipo_documento), ('numero_documento', '=', numero_documento)])
        if paciente:
            diagnostico_vals['paciente_id'] = paciente.id
            diagnostico = self.env['clinica.diagnostico'].create(diagnostico_vals)
            return diagnostico
        else:
            return False

class Acompanante(models.Model):
    _name = 'clinica.acompanante'
    _description = 'Modelo para gestionar acompañantes'

    # Definir los campos para la gestión de acompañantes
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    parentesco = fields.Char(string='Parentesco')
    telefono_contacto = fields.Char(string='Teléfono de Contacto')
    paciente_id = fields.Many2one('clinica.paciente', string='Paciente')

class Diagnostico(models.Model):
    _name = 'clinica.diagnostico'
    _description = 'Modelo para gestionar diagnósticos médicos'

    # Definir los campos para la gestión de diagnósticos
    nombre_diagnostico = fields.Char(string='Diagnóstico', required=True)
    fecha_diagnostico = fields.Date(string='Fecha del Diagnóstico')
    medico_id = fields.Many2one('clinica.medico', string='Médico')
    paciente_id = fields.Many2one('clinica.paciente', string='Paciente')

class Medico(models.Model):
    _name = 'clinica.medico'
    _description = 'Modelo para gestionar médicos'

    # Definir los campos para la gestión de médicos
    name = fields.Char(string='Nombre', required=True)
    matricula = fields.Char(string='Matrícula')

    # Relación uno a muchos con diagnósticos médicos
    diagnosticos_ids = fields.One2many('clinica.diagnostico', 'medico_id', string='Diagnósticos Médicos')
