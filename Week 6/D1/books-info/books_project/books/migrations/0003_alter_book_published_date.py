# Generated by Django 4.2.4 on 2023-08-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_page_count_book_thumbnail_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(max_length=10),
        ),
    ]