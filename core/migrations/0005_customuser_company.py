# Generated by Django 5.1.4 on 2024-12-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_requirement_attachments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
