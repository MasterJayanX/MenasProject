# Generated by Django 4.1.1 on 2022-11-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menapp', '0012_alter_resumen_resumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumen',
            name='usuario',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resumen',
            name='resumen',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
