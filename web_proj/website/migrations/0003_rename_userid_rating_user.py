# Generated by Django 4.2.7 on 2023-12-09 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_rating_opinion_alter_rating_userid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='userId',
            new_name='user',
        ),
    ]
