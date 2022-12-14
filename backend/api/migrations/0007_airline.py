# Generated by Django 4.1.1 on 2022-12-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Airline",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("airline", models.CharField(max_length=30)),
                ("departure_time", models.CharField(max_length=30)),
                ("destination_time", models.CharField(max_length=30)),
                ("price", models.CharField(max_length=30)),
                ("stops", models.CharField(max_length=30)),
                ("duration", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "Airlines",
            },
        ),
    ]
