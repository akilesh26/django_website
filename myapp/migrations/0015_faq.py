# Generated by Django 5.1.1 on 2024-09-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_remove_portfolio_number_alter_portfolio_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faq",
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
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=200)),
            ],
        ),
    ]