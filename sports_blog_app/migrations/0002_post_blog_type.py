# Generated by Django 2.1.4 on 2019-01-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_type',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]