# Generated by Django 3.0.3 on 2020-05-18 23:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0002_participante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
