# Generated by Django 2.1 on 2020-09-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoteLinux', '0002_auto_20191206_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlinux',
            name='linux_app',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='newlinux',
            name='linux_hostname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='newlinux',
            name='linux_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
