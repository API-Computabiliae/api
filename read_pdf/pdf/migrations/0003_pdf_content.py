# Generated by Django 4.2.6 on 2023-10-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_alter_pdf_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
