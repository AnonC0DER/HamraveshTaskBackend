# Generated by Django 4.1.3 on 2022-11-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='status',
            field=models.CharField(choices=[('running', 'Running'), ('finished', 'Finished')], default='finished', max_length=20),
        ),
    ]
