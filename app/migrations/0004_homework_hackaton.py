# Generated by Django 4.0 on 2024-04-26 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_student_group_group_student_student_coin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='homework/')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('coins', models.IntegerField(default=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group')),
            ],
        ),
        migrations.CreateModel(
            name='Hackaton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('day', models.DateField()),
                ('file', models.FileField(upload_to='')),
                ('coins', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]