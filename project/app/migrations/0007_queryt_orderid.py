# Generated by Django 5.0 on 2024-01-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_query_queryt_query_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryt',
            name='OrderId',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
