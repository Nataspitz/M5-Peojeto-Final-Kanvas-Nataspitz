# Generated by Django 4.2.6 on 2023-10-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_remove_course_studants"),
        ("students_courses", "0001_initial"),
        ("accounts", "0002_alter_account_password_alter_account_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="my_courses",
            field=models.ManyToManyField(
                related_name="students",
                through="students_courses.StudentsCourse",
                to="courses.course",
            ),
        ),
    ]
