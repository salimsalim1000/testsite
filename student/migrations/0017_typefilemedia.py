# Generated by Django 3.0.7 on 2020-09-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20200906_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeFileMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('typee', models.IntegerField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]