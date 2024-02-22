from odoo import models, fields, api

class Pacientes(models.Model):
    _name = "pacientes"

    name = fields.Char("Nombre")
    apellido = fields.Char("Apellido")
    tipo_documento = fields.Selection([
        ('dni', 'DNI'),
        ('le', 'LE'),
        ('ci', 'CI'),
        ('ce', 'CE'),
        ('pas', 'Pas')
        ('otro', 'Otro')
    ], string="Tipo de Documento")
    numero_documento = fields.Char("Número de Documento")
    fecha_nacimiento = fields.Date("Fecha de Nacimiento")
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')
    ], string="Género")
    direccion = fields.Char("Dirección")
    ciudad = fields.Char("Ciudad")
    codigo_postal = fields.Char("Código Postal")
    telefono = fields.Char("Teléfono")


    def crear_paciente(self, datos_paciente):
    
        # Función que crea un nuevo paciente en el sistema.

        # Parámetros:
        #     datos_paciente (dict): Un diccionario con los datos del paciente,
        #     incluyendo nombre, apellido, tipo/número de documento, etc.

        # Retorno:
        #     Pacientes: El objeto `Pacientes` creado en el sistema.
        paciente = self.env['pacientes'].create(datos_paciente)
        return paciente



class Acompanhantes(models.Model):
    _name = "acompanhantes"

    paciente_id = fields.Many2one("pacientes", string="Paciente")
    nombre = fields.Char("Nombre")
    apellido = fields.Char("Apellido")
    parentesco = fields.Selection([
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('hijo', 'Hijo'),
        ('otro', 'Otro')
    ], string="Parentesco")
    telefono = fields.Char("Teléfono")

class Diagnosticos(models.Model):
    _name = "diagnosticos"

    paciente_id = fields.Many2one("pacientes", string="Paciente")
    diagnostico_id = fields.Many2one("diagnosticos_tabla", string="Diagnóstico")
    fecha_diagnostico = fields.Date("Fecha de Diagnóstico")
    medico_id = fields.Many2one("medicos", string="Médico")

    def asociar_diagnostico_a_paciente(self, paciente_id, datos_diagnostico):
    
        # Función que asocia un diagnóstico a un paciente existente.

        # Parámetros:
        #     paciente_id (int): El ID del paciente al que se asociará el
        #     diagnóstico.
        #     datos_diagnostico (dict): Un diccionario con los datos del
        #     diagnóstico, incluyendo fecha, ID del diagnóstico y datos del
        #     médico.

        # Retorno:
        #     bool: True si la asociación se realizó correctamente, False en caso
        #     contrario.
        
        paciente = self.env['pacientes'].browse(paciente_id)
        diagnostico = self.env['diagnosticos'].create(datos_diagnostico)
        paciente.diagnosticos_ids += diagnostico
        return True


    def obtener_pacientes_por_diagnostico(self, diagnostico_id):

        # Función que busca y devuelve una lista de pacientes asociados a un
        # diagnóstico específico.

        # Parámetros:
        #     diagnostico_id (int): El ID del diagnóstico a buscar.

        # Retorno:
        #     list: Una lista de objetos `Pacientes` que tienen el diagnóstico
        #     especificado.

        pacientes = self.env['pacientes'].search([
            ('diagnosticos_ids', 'in', diagnostico_id)
        ])
        return pacientes



class Medicos(models.Model):
    _name = "medicos"

    nombre = fields.Char("Nombre")
    matricula = fields.Char("Matrícula")

class DiagnosticosTabla(models.Model):
    _name = "diagnosticos_tabla"

    codigo = fields.Char("Código")
    descripcion = fields.Char("Descripción")
