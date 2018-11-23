# Generated by Django 2.1.3 on 2018-11-12 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181112_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegisterTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 12, 12, 19, 54, 463169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 12, 12, 19, 54, 464470, tzinfo=utc)),
        ),
    ]