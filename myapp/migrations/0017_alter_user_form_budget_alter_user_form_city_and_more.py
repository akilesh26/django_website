# Generated by Django 5.1.1 on 2024-09-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_user_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_form",
            name="budget",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="user_form",
            name="city",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user_form",
            name="event_mgr",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="user_form",
            name="services",
            field=models.CharField(max_length=500),
        ),
    ]
