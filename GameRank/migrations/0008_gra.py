# Generated by Django 4.1.3 on 2022-11-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameRank', '0007_delete_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gracz', models.TextField(blank=True, null=True)),
                ('wynik', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]