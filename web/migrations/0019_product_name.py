# Generated by Django 4.1.5 on 2023-02-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_subcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]