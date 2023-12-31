# Generated by Django 4.2.6 on 2023-11-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0005_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
    ]
