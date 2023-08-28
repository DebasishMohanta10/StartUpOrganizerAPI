# Generated by Django 4.2.4 on 2023-08-15 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=31, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A Label for URL config", max_length=31, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Startup",
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
                ("name", models.CharField(db_index=True, max_length=63)),
                ("slug", models.SlugField(max_length=63, unique=True)),
                ("description", models.TextField()),
                ("founded_date", models.DateField(verbose_name="Date Founded")),
                ("contact", models.EmailField(max_length=254)),
                ("website", models.URLField(max_length=255)),
                ("tags", models.ManyToManyField(to="organizer.tag")),
            ],
        ),
        migrations.CreateModel(
            name="NewsLink",
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
                ("title", models.CharField(max_length=63)),
                ("slug", models.SlugField(max_length=31, unique=True)),
                ("pub_date", models.DateField()),
                ("link", models.URLField(max_length=255)),
                (
                    "startup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizer.startup",
                    ),
                ),
            ],
        ),
    ]
