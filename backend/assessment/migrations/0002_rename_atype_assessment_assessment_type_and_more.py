# Generated by Django 4.1.5 on 2023-11-12 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_grade_course_grade_now_course_grade_total_and_more'),
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='atype',
            new_name='assessment_type',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='count',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='grade',
        ),
        migrations.AddField(
            model_name='assessment',
            name='grade_now',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='grade_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='is_counted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='course.course'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]