# Generated by Django 3.1 on 2020-08-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200818_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]