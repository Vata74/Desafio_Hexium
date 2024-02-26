# -*- coding: utf-8 -*-
{
    'name': "Gestión Clínica",
    
    'summary': "Módulo para gestionar pacientes, acompañantes y diagnósticos médicos",
    
    'description': """
        Módulo para gestionar la información de pacientes, acompañantes y diagnósticos médicos en una clínica médica.
    """,

    'author': "Valentin Tamola",


    'data': [
        'security/ir.model.access.csv',
        'views/paciente_view.xml',
        'views/acompanante_view.xml',
        'views/diagnostico_view.xml',
        'views/medico_view.xml',
        'views/menu.xml',
        'views/d_nomenclado_view.xml',
        'data/clinica.d_nomenclado.csv',
        'datos_prueba/clinica.medico.csv',
        'datos_prueba/clinica.diagnostico.csv',
        'datos_prueba/clinica.acompanante.csv',
        'datos_prueba/clinica.paciente.csv',
    ],


    'installable': True,
    'application': True,
    'auto_install': True,
}
