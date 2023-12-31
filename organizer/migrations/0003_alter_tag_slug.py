# Generated by Django 4.2.4 on 2023-08-17 03:09

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("organizer", "0002_alter_newslink_slug_alter_newslink_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                help_text="A Label for URL config",
                max_length=31,
                populate_from=["name"],
                unique=True,
            ),
        ),
    ]
