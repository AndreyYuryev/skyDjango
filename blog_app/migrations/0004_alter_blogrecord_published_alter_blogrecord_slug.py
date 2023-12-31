# Generated by Django 5.0 on 2023-12-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blogrecord_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogrecord',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
    ]
