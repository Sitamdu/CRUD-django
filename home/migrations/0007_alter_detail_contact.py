# Generated by Django 4.1.5 on 2023-12-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_detail_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
