# Generated by Django 5.1.1 on 2024-09-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="banner",
            field=models.ImageField(blank=True, default="fallback.png", upload_to=""),
        ),
    ]
