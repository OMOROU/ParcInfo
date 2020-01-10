# Generated by Django 2.2.2 on 2020-01-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full name ')),
                ('Subject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Prenom ')),
                ('message', models.CharField(blank=True, max_length=100, null=True, verbose_name='nom ')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
    ]