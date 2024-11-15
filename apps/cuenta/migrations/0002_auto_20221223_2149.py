# Generated by Django 4.1.4 on 2022-12-24 02:49
from django.db import migrations
from django.contrib.auth.hashers import make_password

class DatosMigracion:
    @classmethod
    def cargar_datos(cls,apps,schema_editor):
        db_alias = schema_editor.connection.alias
        
        TipoAcceso = apps.get_model('cuenta','TipoAcceso')
        
        cls.acceso_total, created = TipoAcceso.objects.get_or_create(nombre='Acceso Total',slug='acceso-total',
            descripcion='Acceso Total al Sistema')
        print(f'\nAcceso Creado: '+str(cls.acceso_total.nombre))

        cls.acceso_parcial,created = TipoAcceso.objects.get_or_create(nombre='Acceso Parcial',slug='acceso-parcial',
            descripcion='Acceso Parcial al Sistema')
        print(f'Acceso Creado: '+str(cls.acceso_parcial.nombre))

        cls.acceso_denegado,created = TipoAcceso.objects.get_or_create(nombre='Acceso Denegado',slug='acceso-denegado',
            descripcion='Acceso Denegado al Sistema')
        print(f'Acceso Creado: '+str(cls.acceso_denegado.nombre))
        
        
        Role = apps.get_model('cuenta','Role')

        cls.role_superusuario, created = Role.objects.get_or_create(nombre='Super Usuario',slug='super-usuario',
            acceso_id = cls.acceso_total.id,descripcion='Super Usuario del Sistema')
        print(f'Rol Creado: '+str(cls.role_superusuario.nombre))

        cls.role_admin, created = Role.objects.get_or_create(nombre='Administrador',slug='administrador',
            acceso_id = cls.acceso_parcial.id,descripcion='Administrador del Sistema')
        print(f'Rol Creado: '+str(cls.role_admin.nombre))

        cls.role_vendedor, created = Role.objects.get_or_create(nombre='Vendedor',slug='vendedor',
            acceso_id = cls.acceso_parcial.id,descripcion='Vendedor del Sistema')
        print(f'Rol Creado: '+str(cls.role_vendedor.nombre))

        cls.role_invitado, created = Role.objects.get_or_create(nombre='Invitado',slug='invitado',
            acceso_id = cls.acceso_denegado.id,descripcion='Invitado sin privilegios en el sistema')
        print(f'Rol Creado: '+str(cls.role_invitado.nombre))
        
        Sexo = apps.get_model('cuenta','Sexo')

        cls.sexo_m, created = Sexo.objects.get_or_create(nombre = 'Masculino')
        print(f'Género Creado: '+cls.sexo_m.nombre)

        cls.sexo_f, created = Sexo.objects.get_or_create(nombre = 'Femenino')
        print(f'Género Creado: '+str(cls.sexo_f.nombre))

        TipoDocumento = apps.get_model('cuenta','TipoDocumento')

        cls.dni, created = TipoDocumento.objects.get_or_create(tipo='01',nombre_corto='D.N.I/L.E',longitud=8,
            nombre_largo='D.N.I / Libreta Electoral')
        print(f'Tipo Documento Creado: '+str(cls.dni.nombre_corto))

        cls.carnet, created = TipoDocumento.objects.get_or_create(tipo='04',nombre_corto='CARNET EXT.',longitud=12,
            nombre_largo='Carnet de Extranjería')
        print(f'Tipo Documento Creado: '+str(cls.carnet.nombre_corto))

        cls.ruc, created = TipoDocumento.objects.get_or_create(tipo='06',nombre_corto='R.U.C.',longitud=11,
            nombre_largo='Régimen Único del Contribuyente')
        print(f'Tipo Documento Creado: '+str(cls.ruc.nombre_corto))

        cls.pasaporte,created = TipoDocumento.objects.get_or_create(tipo='07',nombre_corto='PASAPORTE',longitud=12,
            nombre_largo='Pasaporte')
        print(f'Tipo Documento Creado: '+str(cls.pasaporte.nombre_corto))

        cls.partida, created = TipoDocumento.objects.get_or_create(tipo='11',nombre_corto='P. NAC.',longitud=15,
            nombre_largo='Partida de Nacimiento')
        print(f'Tipo Documento Creado: '+str(cls.partida.nombre_corto))

        cls.otros, created = TipoDocumento.objects.get_or_create(tipo='00',nombre_corto='OTROS',longitud=15,
            nombre_largo='OTROS')
        print(f'Tipo Documento Creado: '+str(cls.otros.nombre_corto))
        
        Persona = apps.get_model('cuenta','Persona')

        cls.persona_uno,created = Persona.objects.get_or_create(
            tipo_documento_id = cls.dni.id,numero_documento='10000001',nombres="Admin",
            apellido_paterno="Master",apellido_materno='Master',sexo_id=cls.sexo_m.id)
        print(f'Persona Creada: '+str(cls.persona_uno.nombres)+' '+str(cls.persona_uno.apellido_paterno)+' '+str(cls.persona_uno.apellido_materno))
        
        Usuario = apps.get_model('cuenta','Usuario')

        cls.usuario_nuevo, created = Usuario.objects.get_or_create( 
            persona_id = cls.persona_uno.id, username = 'admin',
            password = make_password('123456789'),email = 'master@ejemplo.com')
        print(f'Usuario Creado: '+str(cls.usuario_nuevo.username))

        cls.usuario_nuevo.roles.add(cls.role_superusuario)
        print(f'\nRol '+str(cls.role_superusuario.nombre)+' asignado a '+str(cls.usuario_nuevo.username))
        
    
class Migration(migrations.Migration):
        
    dependencies = [
        ('cuenta', '0003_remove_persona_apellidos_persona_apellido_materno_and_more'),
    ]

    operations = [
        migrations.RunPython(DatosMigracion.cargar_datos)
    ]
