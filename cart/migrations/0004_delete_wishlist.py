# Generated by Django 3.2.2 on 2021-05-22 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]