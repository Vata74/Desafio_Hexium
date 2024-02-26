{
    'name': "Gestión Clínica",
    
    'summary': "Módulo para gestionar pacientes, acompañantes y diagnósticos médicos",
    
    'description': """
        Módulo para gestionar la información de pacientes, acompañantes y diagnósticos médicos en una clínica médica.
    """,

    'author': "Valentin Tamola",

    'data': [
        'security/ir.model.access.csv',  # Archivo CSV para definir los permisos de acceso a los modelos
        'views/paciente_view.xml',  # Vista XML para la interfaz de gestión de pacientes
        'views/acompanante_view.xml',  # Vista XML para la interfaz de gestión de acompañantes
        'views/diagnostico_view.xml',  # Vista XML para la interfaz de gestión de diagnósticos médicos
        'views/medico_view.xml',  # Vista XML para la interfaz de gestión de médicos
        'views/menu.xml',  # Vista XML para definir el menú del módulo
        'views/d_nomenclado_view.xml',  # Vista XML para la interfaz de gestión de nomenclaturas de diagnósticos
        'data/clinica.d_nomenclado.csv',  # Archivo CSV para cargar datos de nomenclaturas de diagnósticos
        'datos_prueba/clinica.medico.csv',  # Archivo CSV para cargar datos de médicos de prueba
        'datos_prueba/clinica.diagnostico.csv',  # Archivo CSV para cargar datos de diagnósticos de prueba
        'datos_prueba/clinica.acompanante.csv',  # Archivo CSV para cargar datos de acompañantes de prueba
        'datos_prueba/clinica.paciente.csv',  # Archivo CSV para cargar datos de pacientes de prueba
    ],

    'installable': True,
    'application': True,
    'auto_install': True,
}
