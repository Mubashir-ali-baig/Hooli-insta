# Generated by Django 3.0.3 on 2020-02-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
