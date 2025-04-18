# Generated by Django 5.2 on 2025-04-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_logo_socialmedialink_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('category_name',),
            },
        ),
    ]
