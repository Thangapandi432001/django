# Generated by Django 5.1.2 on 2024-11-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_image_name_alter_image_i_1_alter_image_i_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_2', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='i_2',
        ),
    ]