# Generated by Django 2.1 on 2019-11-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewLinux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linux_ip', models.CharField(max_length=100)),
                ('linux_port', models.CharField(max_length=100)),
                ('linux_user', models.CharField(max_length=100)),
                ('linux_passwd', models.CharField(max_length=100)),
            ],
        ),
    ]
