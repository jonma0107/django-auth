# Generated by Django 4.0 on 2023-02-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
