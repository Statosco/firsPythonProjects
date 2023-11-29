# Generated by Django 4.2.5 on 2023-10-12 05:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("new", "0003_alter_room_options_room_participant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="participant",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]