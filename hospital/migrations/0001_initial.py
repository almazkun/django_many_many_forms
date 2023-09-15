# Generated by Django 4.2.4 on 2023-09-15 06:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("age", models.IntegerField()),
                ("sex", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="BloodType",
            fields=[
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="hospital.patient",
                    ),
                ),
                (
                    "value",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "A"), (1, "B"), (2, "AB"), (3, "O")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ecog",
            fields=[
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="hospital.patient",
                    ),
                ),
                (
                    "value",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "ECOG 0"),
                            (1, "ECOG 1"),
                            (2, "ECOG 2"),
                            (3, "ECOG 3"),
                            (4, "ECOG 4"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Imaging",
            fields=[
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="hospital.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageryType",
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
                (
                    "value",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "CT"), (1, "PET"), (2, "EBUS"), (3, "Other")]
                    ),
                ),
                (
                    "imaging",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="types",
                        to="hospital.imaging",
                    ),
                ),
            ],
        ),
    ]
