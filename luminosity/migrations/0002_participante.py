# Generated by Django 3.0.3 on 2020-05-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(verbose_name='cedula')),
                ('nombre', models.CharField(max_length=30)),
                ('actividad', models.CharField(max_length=30)),
                ('estrato', models.IntegerField(verbose_name='estrato')),
            ],
        ),
    ]
