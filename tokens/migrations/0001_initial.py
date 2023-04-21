# Generated by Django 4.2 on 2023-04-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TokenAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=10, unique=True)),
                ('play_tokens', models.IntegerField(default=0)),
                ('gift_tokens', models.IntegerField(default=0)),
            ],
        ),
    ]
