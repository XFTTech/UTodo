# Generated by Django 4.1.5 on 2023-11-12 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_rename_atype_assessment_assessment_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='is_counted',
        ),
    ]
