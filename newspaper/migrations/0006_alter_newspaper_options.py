# Generated by Django 4.2.7 on 2023-11-23 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_alter_redactor_year_of_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newspaper',
            options={'ordering': ['published_date']},
        ),
    ]