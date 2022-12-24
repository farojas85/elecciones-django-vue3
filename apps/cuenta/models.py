from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
import os
# Create your models here.

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    nombre = models.CharField(max_length=191,help_text="Nombre del Menú")
    enlace = models.CharField(max_length=191,help_text="Ruta Menú")
    icono = models.CharField(max_length=191, blank=True, null=True,help_text="Icono del Menú")
    padre = models.IntegerField(default=0,help_text="Padre del Menú")
    orden = models.SmallIntegerField(blank=True, null=True,help_text="Orden de menú")
    es_activo = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='menus'

    def __str__(self):
        return '{}'.format(self.nombre)


class Permiso(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    nombre = models.CharField(max_length=191,help_text="Nombre de Acceso")
    slug = models.CharField(help_text="Ruta Amigable Acceso", max_length=191)
    descripcion = models.CharField(help_text="Descripción de Acceso", max_length=191, blank=True, null=True)
    es_activo = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='permisos'

    def __str__(self):
        return '{}'.format(self.nombre)


class TipoAcceso(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    nombre = models.CharField(max_length=191,help_text="Nombre de Acceso")
    slug = models.CharField(help_text="Ruta Amigable Acceso", max_length=191)
    descripcion = models.CharField(help_text="Descripción de Acceso", max_length=191, blank=True, null=True)
    es_activo = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='tipo_accesos'

    def __str__(self):
        return '{}'.format(self.nombre)
    
    
class Role(models.Model):
    nombre = models.CharField(max_length=191, blank=True, null=True,help_text="Nombre de Rol")
    slug = models.CharField(max_length=191, blank=True, null=True,help_text="Ruta Amigable Rol")
    descripcion = models.CharField(max_length=191, blank=True, null=True,help_text="Descripción de Rol")
    acceso = models.ForeignKey(TipoAcceso, on_delete=models.RESTRICT,help_text="Persona Usuario",blank=True,null = True)
    es_activo = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)
    permisos = models.ManyToManyField(Permiso)
    menus = models.ManyToManyField(Menu)

    class Meta:
        verbose_name_plural='roles'

    def __str__(self):
        return '{}'.format(self.nombre)


class TipoDocumento(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    tipo = models.CharField(max_length=2, blank=True, null=True,help_text='Código Tipo Documento')
    nombre_corto = models.CharField(max_length=191,blank=True, null=True,help_text="Descripción Corta")
    nombre_largo = models.CharField(max_length=191,blank=True, null=True,help_text="Descripción Larga")
    longitud = models.PositiveSmallIntegerField(help_text="Longitud Documento")
    fecha_creada = models.DateTimeField(auto_now_add=True, help_text="Fecha Creada")
    fecha_modificada = models.DateTimeField(auto_now=True, help_text="Fecha Eliminada")
    fecha_eliminada = models.DateTimeField(blank=True, null=True,help_text="Fecha Eliminada")

    class Meta:
        verbose_name_plural='tipo_documentos'

    def __str__(self):
        return '{}'.format(self.nombre_corto)
    

class Sexo(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    nombre = models.CharField(max_length=191,help_text="Descripción Sexo")
    fecha_creada = models.DateTimeField(auto_now_add=True, help_text="Fecha Creada")
    fecha_modificada = models.DateTimeField(auto_now=True, help_text="Fecha Eliminada")
    fecha_eliminada = models.DateTimeField(blank=True, null=True,help_text="Fecha Eliminada")
    
    class Meta:
        verbose_name_plural='sexos'
    
    def __str__(self):
        return '{}'.format(self.nombre)


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.RESTRICT, blank=True, null=True)
    numero_documento = models.CharField(max_length=15,help_text="Número Documento")
    nombres = models.CharField(max_length=191,help_text="Nombres")
    apellido_paterno = models.CharField(max_length=191,help_text='Apellidos',blank=True, null=True)
    apellido_materno = models.CharField(max_length=191,help_text='Apellidos',blank=True, null=True)
    telefono = models.CharField(max_length=50,blank=True, null=True,help_text="Teléfono")
    direccion = models.CharField(max_length=191,blank=True, null=True,help_text="Dirección")
    sexo = models.ForeignKey(Sexo, on_delete=models.RESTRICT, blank=True, null=True,help_text="Sexo Persona")
    fecha_creada = models.DateTimeField(auto_now_add=True, help_text="Fecha Creada")
    fecha_modificada = models.DateTimeField(auto_now=True, help_text="Fecha Eliminada")
    fecha_eliminada = models.DateTimeField(blank=True, null=True,help_text="Fecha Eliminada")
    
    class Meta:
        verbose_name_plural= 'personas'

    def __str__(self):
        return '{0} {1}'.format(self.nombres,self.apellidos)


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un Correo Electrónico")
        
        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()

        return user
    
    
    def create_superuser(self,email,password, **extra_fields):
        user = self.create_user(email,password,**extra_fields)
        
        user.is_superuser = True
        user.save()
        
        return user
    
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    persona =  models.OneToOneField(Persona, on_delete=models.RESTRICT,help_text="Persona Usuario",blank=True,null = True)
    email = models.EmailField(help_text="Correo Electrónico", max_length=191,unique=True,blank=True, null=True)
    username = models.CharField(max_length=191,unique=True,help_text="Nombre Usuario")
    imagen  = models.ImageField(max_length=191,help_text="Imagen de Perfil",upload_to="media/usuarios/", blank=True,null=True)
    es_activo = models.BooleanField(default=True)
    last_login =models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=191,blank=True,null=True)
    objects = UsuarioManager()
    roles = models.ManyToManyField(Role)
    fecha_creada = models.DateTimeField(auto_now_add=True, help_text="Fecha Creada")
    fecha_modificada = models.DateTimeField(auto_now=True, help_text="Fecha Eliminada")
    fecha_eliminada = models.DateTimeField(blank=True, null=True,help_text="Fecha Eliminada")
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELD=['username','email']
    
    def __str__(self):
        return '{}'.format(self.username)
    
    def get_user(self):
        return self.usename
        
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username

    @property
    def is_active(self):
        return self.es_activo