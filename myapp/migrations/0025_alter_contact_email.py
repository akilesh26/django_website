# Generated by Django 5.1.1 on 2024-09-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0024_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]