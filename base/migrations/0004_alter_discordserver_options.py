# Generated by Django 4.1.4 on 2023-12-14 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_discordserver_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discordserver',
            options={'ordering': ['server_id', 'auth_code']},
        ),
    ]
