# Generated by Django 4.0.3 on 2022-04-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_rename_supers_super'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='second_ability',
            new_name='secondary_ability',
        ),
    ]
