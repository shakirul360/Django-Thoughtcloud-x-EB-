# Generated by Django 3.1.4 on 2020-12-26 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retrospection', '0003_thought_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thought',
            name='manager',
        ),
    ]
