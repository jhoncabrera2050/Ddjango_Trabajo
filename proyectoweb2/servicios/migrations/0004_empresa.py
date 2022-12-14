# Generated by Django 4.1.1 on 2022-09-26 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_rename_image_servicio_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
