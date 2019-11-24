# Generated by Django 2.2.6 on 2019-11-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_num', models.IntegerField()),
                ('genre_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField()),
                ('title', models.TextField()),
                ('original_title', models.TextField()),
                ('popularity', models.FloatField()),
                ('runtime', models.IntegerField()),
                ('release_date', models.DateField()),
                ('credit', models.TextField()),
                ('genres', models.TextField()),
            ],
        ),
    ]
