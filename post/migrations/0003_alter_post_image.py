# Generated by Django 4.2.4 on 2023-08-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_created_post_draft_post_image_post_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/post'),
        ),
    ]
