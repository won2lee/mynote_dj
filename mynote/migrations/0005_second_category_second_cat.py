# Generated by Django 3.1.7 on 2021-03-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0004_auto_20210307_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='second_category',
            name='second_cat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
