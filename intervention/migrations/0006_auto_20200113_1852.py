# Generated by Django 2.2.2 on 2020-01-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0005_auto_20200113_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panne',
            name='niveau',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Niveau de la panne'),
        ),
    ]
