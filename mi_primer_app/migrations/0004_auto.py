# Generated by Django 5.2.4 on 2025-07-31 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_primer_app', '0003_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
