# Generated by Django 3.2.7 on 2021-09-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_register_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
