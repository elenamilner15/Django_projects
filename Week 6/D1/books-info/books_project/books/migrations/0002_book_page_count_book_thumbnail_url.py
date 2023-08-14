# Generated by Django 4.2.4 on 2023-08-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail_url',
            field=models.URLField(default=''),
        ),
    ]
