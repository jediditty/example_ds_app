# Generated by Django 2.2 on 2019-04-30 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elastic_api', '0002_datatobe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_1',
            new_name='field_1_int',
        ),
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_2',
            new_name='field_2_char',
        ),
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_3',
            new_name='field_3_float',
        ),
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_4',
            new_name='field_4_float',
        ),
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_5',
            new_name='field_5_char',
        ),
        migrations.RenameField(
            model_name='datatobe',
            old_name='field_6',
            new_name='field_6_int',
        ),
    ]