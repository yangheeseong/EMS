# Generated by Django 4.0.3 on 2022-07-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_remove_task_manager1_remove_task_manager2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceType', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteType', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='deviceType',
        ),
        migrations.RemoveField(
            model_name='task',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='task',
            name='siteType',
        ),
        migrations.AddField(
            model_name='task',
            name='deviceType',
            field=models.ManyToManyField(blank=True, to='task.devicetype'),
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ManyToManyField(blank=True, to='task.manager'),
        ),
        migrations.AddField(
            model_name='task',
            name='siteType',
            field=models.ManyToManyField(blank=True, to='task.sitetype'),
        ),
    ]
