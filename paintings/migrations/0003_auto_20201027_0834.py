# Generated by Django 3.1.2 on 2020-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0002_auto_20201027_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintings',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]