# Generated by Django 4.2.4 on 2023-08-20 04:28

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("organizer", "0004_alter_startup_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newslink",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=31,
                populate_from=["title"],
                unique=True,
            ),
        ),
    ]