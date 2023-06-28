# Generated by Django 4.2.2 on 2023-06-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_microorganism_img_alter_microorganism_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturemedia',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='microorganism',
            name='characteristics',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='microorganism',
            name='description',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='microorganism',
            name='laboratory_diagnosis',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='microorganism',
            name='manifestation',
            field=models.TextField(max_length=3000),
        ),
        migrations.CreateModel(
            name='MorphologicalClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('culture_medias', models.ManyToManyField(to='main_app.culturemedia')),
            ],
        ),
    ]