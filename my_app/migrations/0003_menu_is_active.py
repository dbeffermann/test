# Generated by Django 3.0.7 on 2020-06-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200614_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]