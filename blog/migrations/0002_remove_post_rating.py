# Generated by Django 5.2.1 on 2025-05-24 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="rating",
        ),
    ]
