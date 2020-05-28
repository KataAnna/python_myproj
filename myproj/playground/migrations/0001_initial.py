# Generated by Django 3.0.6 on 2020-05-18 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('pass_id', models.CharField(max_length=10, unique=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='info', serialize=False, to='playground.Student')),
            ],
            options={
                'verbose_name': 'StudentInfo',
                'verbose_name_plural': 'StudentInfos',
            },
        ),
    ]