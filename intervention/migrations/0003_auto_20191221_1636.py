# Generated by Django 2.2.2 on 2019-12-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0002_auto_20191117_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type_panne',
            name='designation',
        ),
        migrations.AddField(
            model_name='panne',
            name='libelle_pan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='libelle de la panne'),
        ),
        migrations.AddField(
            model_name='type_panne',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='description type de panne'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date_interv',
            field=models.DateField(blank=True, null=True, verbose_name="date de l'intervention"),
        ),
        migrations.AlterField(
            model_name='type_panne',
            name='libelle_pan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='libelle de la panne'),
        ),
    ]
