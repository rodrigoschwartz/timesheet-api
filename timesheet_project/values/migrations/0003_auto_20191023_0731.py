# Generated by Django 2.1 on 2019-10-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0002_auto_20191023_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
