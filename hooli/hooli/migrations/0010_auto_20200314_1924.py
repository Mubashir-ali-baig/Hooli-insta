# Generated by Django 3.0.3 on 2020-03-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooli', '0009_phototag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phototag',
            name='coords',
            field=models.CharField(max_length=40),
        ),
    ]
