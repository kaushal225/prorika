# Generated by Django 4.1.7 on 2023-03-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrika', '0002_alter_problem_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]