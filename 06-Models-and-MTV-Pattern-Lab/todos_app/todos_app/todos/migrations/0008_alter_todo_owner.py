# Generated by Django 3.2.4 on 2021-06-08 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.person'),
        ),
    ]
