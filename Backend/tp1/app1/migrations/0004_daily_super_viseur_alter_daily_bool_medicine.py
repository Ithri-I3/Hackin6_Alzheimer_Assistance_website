# Generated by Django 5.0.2 on 2024-02-23 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_lieu_daily_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='super_viseur',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app1.super_viseur'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daily',
            name='bool',
            field=models.CharField(default='false', max_length=100),
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Time_medecine', models.CharField(max_length=100)),
                ('bool', models.CharField(default='false', max_length=100)),
                ('super_viseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.super_viseur')),
            ],
        ),
    ]
