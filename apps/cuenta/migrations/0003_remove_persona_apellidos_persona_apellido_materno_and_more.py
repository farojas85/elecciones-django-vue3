# Generated by Django 4.1.4 on 2022-12-24 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='apellidos',
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido_materno',
            field=models.CharField(blank=True, help_text='Apellidos', max_length=191, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido_paterno',
            field=models.CharField(blank=True, help_text='Apellidos', max_length=191, null=True),
        ),
    ]