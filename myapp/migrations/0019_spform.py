# Generated by Django 5.1.1 on 2024-09-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0018_rename_user_form_userform"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpForm",
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
                ("name", models.CharField(max_length=100)),
                ("stype", models.CharField(max_length=100)),
                ("desc", models.CharField(max_length=500)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
