# Generated by Django 3.0.7 on 2020-10-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_degreycompany_withdegreycomp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degreycompany',
            name='withdegreycomp',
        ),
    ]
