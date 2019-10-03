# Generated by Django 2.2.5 on 2019-10-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0001_initial'),
        ('hours', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hours',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hours.Hours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='values',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='values.Values'),
            preserve_default=False,
        ),
    ]
