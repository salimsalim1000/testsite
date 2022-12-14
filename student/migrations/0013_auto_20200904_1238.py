# Generated by Django 3.0.7 on 2020-09-04 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200903_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='otheractiv',
            name='titel',
        ),
        migrations.AlterField(
            model_name='filemediamoy',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='filemediamoy',
            name='titel',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='filemediamoy',
            name='type',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='filemediasec',
            name='date',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='filemediasec',
            name='titel',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='otheractiv',
            name='date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='otheractiv',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.ActiviteName'),
            preserve_default=False,
        ),
    ]
