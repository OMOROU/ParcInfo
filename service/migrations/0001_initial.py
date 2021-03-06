# Generated by Django 2.2.2 on 2019-11-06 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dep', models.PositiveSmallIntegerField(verbose_name='numéro du departement')),
                ('libelle_dep', models.CharField(choices=[('COMPTABILITE', 'COMPTABILITE'), ('COMMUNICATION', 'COMMUNICATION'), ('INFORMATIQUE', 'INFORMATIQUE'), ('MARKETING', 'MARKETING'), ('RESEAUX', 'RESEAUX')], default=[0], max_length=100, verbose_name='le type du departement')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description du Departement')),
            ],
            options={
                'verbose_name': 'Departement',
                'verbose_name_plural': 'Departements',
            },
        ),
        migrations.CreateModel(
            name='Intervenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_intervenant', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Identifiant de l'informaticien")),
                ('nom_intervenant', models.CharField(blank=True, max_length=100, null=True, verbose_name="nom de l'informaticien")),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='couriel')),
            ],
            options={
                'verbose_name': 'Intervenant',
                'verbose_name_plural': 'Intervenants',
            },
        ),
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bureau', models.CharField(blank=True, max_length=100, null=True, verbose_name='Identifiant du Bureau')),
                ('num_bureau', models.PositiveSmallIntegerField(verbose_name='numéro du Bureau')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departement', to='service.Departement')),
            ],
            options={
                'verbose_name': 'Bureau',
                'verbose_name_plural': 'Bureaux',
            },
        ),
    ]
