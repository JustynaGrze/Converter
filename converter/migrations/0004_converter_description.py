# Generated by Django 3.1.3 on 2020-11-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_auto_20201121_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='converter',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
