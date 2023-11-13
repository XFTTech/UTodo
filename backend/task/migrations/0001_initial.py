# Generated by Django 4.1.5 on 2023-11-12 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField()),
                ('grade', models.FloatField()),
                ('title', models.CharField(max_length=200)),
                ('is_chosen', models.BooleanField(default=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='assessment.assessment')),
            ],
        ),
    ]