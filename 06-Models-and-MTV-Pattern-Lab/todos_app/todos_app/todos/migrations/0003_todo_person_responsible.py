# Generated by Django 3.2.4 on 2021-06-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='person_responsible',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
