# Generated by Django 2.2.2 on 2019-12-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20191211_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='num_bureau',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='numéro du Bureau'),
        ),
    ]