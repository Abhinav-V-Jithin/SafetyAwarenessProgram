# Generated by Django 4.0.2 on 2022-02-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipyardGiftProject', '0005_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='pc_no',
            field=models.CharField(default='', max_length=30),
        ),
    ]