# Generated by Django 4.0.4 on 2022-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_rename_userextend_userextendcreateview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='oras',
            field=models.CharField(choices=[('SIBIU', 'SIBIU'), ('BRASOV', 'BRASOV'), ('CLUJ', 'CLUJ')], default='', max_length=30),
            preserve_default=False,
        ),
    ]
