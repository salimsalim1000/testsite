# Generated by Django 3.0.7 on 2020-09-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_otheractiv_withuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemediasec',
            name='date',
            field=models.DateField(),
        ),
    ]
