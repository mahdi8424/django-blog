# Generated by Django 5.2.1 on 2025-05-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_tag_remove_author_contact_author_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("text", models.TextField()),
            ],
        ),
    ]
