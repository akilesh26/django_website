# Generated by Django 5.1.1 on 2024-09-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_delete_pricing"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("review", models.CharField(max_length=500)),
                ("reviewer_name", models.CharField(max_length=100)),
                ("reviewer_designation", models.CharField(max_length=100)),
                (
                    "reviewer_image",
                    models.ImageField(blank=True, default="fallback.png", upload_to=""),
                ),
            ],
        ),
    ]