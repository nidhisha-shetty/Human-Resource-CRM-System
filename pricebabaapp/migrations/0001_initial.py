# Generated by Django 3.1.4 on 2020-12-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricebaba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=9999999999)),
                ('age', models.IntegerField(max_length=100)),
                ('dob', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]