# Generated by Django 4.1 on 2023-08-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LApp', '0003_alter_leave_leaveatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='appldate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='enddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(),
        ),
    ]
