# Generated by Django 4.2.9 on 2024-01-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_talentaccount_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentaccount',
            name='greeting',
            field=models.TextField(null=True),
        ),
    ]