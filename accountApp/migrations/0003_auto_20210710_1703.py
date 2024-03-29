# Generated by Django 3.2.5 on 2021-07-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0002_address_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='pic.png', null=True, upload_to='user_profile'),
        ),
    ]
