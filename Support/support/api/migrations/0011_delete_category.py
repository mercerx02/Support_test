# Generated by Django 4.0.4 on 2022-05-11 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
