# Generated by Django 4.0.4 on 2022-07-20 08:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translators', '0009_alter_chapter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Title must be longer than 5 characters')]),
        ),
    ]
