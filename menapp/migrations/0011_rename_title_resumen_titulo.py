# Generated by Django 4.1.1 on 2022-11-10 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menapp', '0010_rename_titulo_resumen_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumen',
            old_name='title',
            new_name='titulo',
        ),
    ]
