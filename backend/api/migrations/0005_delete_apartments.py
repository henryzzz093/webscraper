# Generated by Django 4.1.1 on 2022-11-05 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_apartments_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Apartments",
        ),
    ]
