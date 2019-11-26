# Generated by Django 2.2.7 on 2019-11-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.IntegerField()),
                ('images', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('overview', models.TextField()),
                ('original_title', models.TextField()),
                ('popularity', models.FloatField()),
                ('runtime', models.IntegerField()),
                ('release_date', models.DateField()),
                ('credit', models.TextField()),
                ('genres', models.TextField()),
                ('poster', models.TextField()),
                ('videos', models.TextField()),
            ],
        ),
    ]
