# Generated by Django 4.1.7 on 2023-03-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrika', '0003_alter_problem_created_at_alter_problem_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
