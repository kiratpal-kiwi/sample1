# Generated by Django 4.1.5 on 2023-02-01 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_loginpage_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('contact', models.IntegerField()),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='web.subscription')),
            ],
        ),
    ]
