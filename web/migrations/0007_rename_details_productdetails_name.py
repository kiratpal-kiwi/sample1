# Generated by Django 4.1.5 on 2023-02-02 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_productdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetails',
            old_name='details',
            new_name='name',
        ),
    ]