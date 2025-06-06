# Generated by Django 5.2.1 on 2025-05-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=10),
        ),
    ]
