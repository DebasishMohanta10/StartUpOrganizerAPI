# Generated by Django 4.2.4 on 2023-08-17 03:08

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("organizer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newslink",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=31,
                populate_from=["name"],
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="newslink",
            name="title",
            field=models.CharField(max_length=31),
        ),
    ]
