# Generated by Django 2.1.5 on 2019-04-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]