# Generated by Django 4.0.2 on 2022-02-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service_created_at_service_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
