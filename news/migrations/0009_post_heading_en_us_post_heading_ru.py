# Generated by Django 4.1.3 on 2023-02-01 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_rename_name_af_category_name_en_us_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heading_en_us',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='heading_ru',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
