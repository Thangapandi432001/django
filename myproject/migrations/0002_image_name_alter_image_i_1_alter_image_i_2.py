# Generated by Django 5.1.2 on 2024-11-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='pandi', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='i_1',
            field=models.ImageField(upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='image',
            name='i_2',
            field=models.ImageField(upload_to='pic'),
        ),
    ]
