# Generated by Django 4.1.1 on 2022-11-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menapp', '0011_rename_title_resumen_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumen',
            name='resumen',
            field=models.TextField(max_length=1000),
        ),
    ]