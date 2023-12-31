# Generated by Django 4.2.2 on 2023-07-01 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CultureMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Microorganism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('img', models.CharField(max_length=600)),
                ('characteristics', models.TextField(max_length=3000)),
                ('description', models.TextField(max_length=3000)),
                ('manifestation', models.TextField(max_length=3000)),
                ('laboratory_diagnosis', models.TextField(max_length=3000)),
                ('verified_microorganism', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MorphologicalClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('culture_medias', models.ManyToManyField(to='main_app.culturemedia')),
            ],
        ),
        migrations.AddField(
            model_name='culturemedia',
            name='microorganism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='culture_medias', to='main_app.microorganism'),
        ),
    ]
