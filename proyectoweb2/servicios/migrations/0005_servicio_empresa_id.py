# Generated by Django 4.1.1 on 2022-09-26 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='empresa_id',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='servicios.empresa'),
            preserve_default=False,
        ),
    ]
