# Generated by Django 4.1.5 on 2023-02-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_delete_loginpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=20)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
    ]
