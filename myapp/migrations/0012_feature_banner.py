# Generated by Django 5.1.1 on 2024-09-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_alter_portfolio_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="banner",
            field=models.ImageField(blank=True, default="fallback.png", upload_to=""),
        ),
    ]
