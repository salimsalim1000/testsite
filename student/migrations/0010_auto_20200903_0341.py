# Generated by Django 3.0.7 on 2020-09-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20200903_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamoyparnt',
            name='nomberesteda',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='mediamoyparnt',
            name='nomberhodor',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='mediasecparnt',
            name='nomberesteda',
            field=models.PositiveIntegerField(blank=1, null=1),
        ),
        migrations.AlterField(
            model_name='mediasecparnt',
            name='nomberhodor',
            field=models.PositiveIntegerField(blank=1, null=1),
        ),
    ]