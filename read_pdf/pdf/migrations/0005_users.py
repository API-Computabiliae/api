# Generated by Django 4.2.6 on 2023-11-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_remove_pdf_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
