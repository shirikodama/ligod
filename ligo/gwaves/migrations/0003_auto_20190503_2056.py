# Generated by Django 2.1.4 on 2019-05-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwaves', '0002_auto_20190503_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gwave',
            name='received_at',
            field=models.IntegerField(default=0),
        ),
    ]