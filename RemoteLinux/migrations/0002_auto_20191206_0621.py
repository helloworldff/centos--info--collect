# Generated by Django 2.1 on 2019-12-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoteLinux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlinux',
            name='linux_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='newlinux',
            table='linux-info',
        ),
    ]
