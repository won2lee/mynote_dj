# Generated by Django 3.1.7 on 2021-03-07 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Second_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat2', models.CharField(blank=True, max_length=100, null=True)),
                ('cat1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mynote.first_category')),
            ],
        ),
    ]
