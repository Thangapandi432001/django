# Generated by Django 5.1.2 on 2024-11-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_pan_remove_image_i_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='pan',
            name='name',
            field=models.CharField(default='pandi', max_length=100),
        ),
    ]