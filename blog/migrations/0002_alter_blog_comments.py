# Generated by Django 5.0.4 on 2024-04-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='blog.comment'),
        ),
    ]