# Generated by Django 4.0.3 on 2022-07-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='memoName',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
