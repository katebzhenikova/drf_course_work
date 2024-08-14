# Generated by Django 5.0.7 on 2024-08-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0007_habitperiodicity_remove_habit_periodicity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habitperiodicity",
            name="period",
            field=models.CharField(
                blank=True,
                choices=[("DAILY", "Ежедневно"), ("WEEKLY", "Еженедельно")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="habitperiodicity",
            name="name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MON", "Понедельник"),
                    ("TUE", "Вторник"),
                    ("WED", "Среда"),
                    ("THU", "Четверг"),
                    ("FRI", "Пятница"),
                    ("SAT", "Суббота"),
                    ("SUN", "Воскресенье"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
