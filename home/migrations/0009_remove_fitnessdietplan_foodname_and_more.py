# Generated by Django 4.2.8 on 2025-05-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_fitnessplan_calories_remove_fitnessplan_carbs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessdietplan',
            name='foodname',
        ),
        migrations.RemoveField(
            model_name='fitnessdietplan',
            name='quantity',
        ),
        migrations.AddField(
            model_name='fitnessdietplan',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
