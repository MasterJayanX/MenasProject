# Generated by Django 4.1.1 on 2022-11-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menapp', '0007_pomodoro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumen', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cronometro',
        ),
    ]
