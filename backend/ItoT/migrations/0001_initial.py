# Generated by Django 4.0.1 on 2022-01-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=1000000, null=True, verbose_name='image_url')),
                ('text', models.CharField(max_length=1000, null=True, verbose_name='text')),
            ],
        ),
    ]
