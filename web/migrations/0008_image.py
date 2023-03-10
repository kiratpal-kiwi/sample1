# Generated by Django 4.1.5 on 2023-02-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_details_productdetails_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/')),
                ('image_name', models.ManyToManyField(blank=True, to='web.productdetails')),
            ],
        ),
    ]
