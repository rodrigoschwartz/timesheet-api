# Generated by Django 2.2.5 on 2019-10-02 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191002_1437'),
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hours',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
            preserve_default=False,
        ),
    ]
