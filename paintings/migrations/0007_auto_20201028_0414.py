# Generated by Django 3.1.2 on 2020-10-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0006_auto_20201027_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paintings',
            name='images',
        ),
        migrations.AddField(
            model_name='paintings',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
