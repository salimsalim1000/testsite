# Generated by Django 3.0.7 on 2020-09-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20200909_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediasec',
            name='date',
            field=models.DateField(),
        ),
    ]
