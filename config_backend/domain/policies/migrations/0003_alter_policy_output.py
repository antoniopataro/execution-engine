# Generated by Django 4.2.5 on 2023-09-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_policy_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='output',
            field=models.BooleanField(default=True),
        ),
    ]
