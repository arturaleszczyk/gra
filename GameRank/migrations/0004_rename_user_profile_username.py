# Generated by Django 4.1.3 on 2022-11-15 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameRank', '0003_rename_rating_gamerank1_ranking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
