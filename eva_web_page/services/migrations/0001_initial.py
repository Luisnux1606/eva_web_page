# Generated by Django 3.0.6 on 2020-05-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitulo')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='projects', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha modificacion')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]