# Generated by Django 4.0.2 on 2022-02-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipyardGiftProject', '0002_author_alter_quote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('attempts', models.IntegerField()),
            ],
        ),
    ]
