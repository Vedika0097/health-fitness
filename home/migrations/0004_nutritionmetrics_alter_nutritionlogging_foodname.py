# Generated by Django 4.2.8 on 2025-04-13 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_nutritionlogging_calories_nutritionlogging_carbs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionMetrics',
            fields=[
                ('foodname', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('carbs', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('sugar', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'NutritionMetrics',
                'verbose_name_plural': 'NutritionMetrics',
            },
        ),
        migrations.AlterField(
            model_name='nutritionlogging',
            name='foodname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.nutritionmetrics'),
        ),
    ]
