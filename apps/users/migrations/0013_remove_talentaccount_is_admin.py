# Generated by Django 4.2.9 on 2024-01-25 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_talentaccount_contact_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talentaccount',
            name='is_admin',
        ),
    ]