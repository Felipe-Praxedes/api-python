# Generated by Django 4.2.3 on 2023-07-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
