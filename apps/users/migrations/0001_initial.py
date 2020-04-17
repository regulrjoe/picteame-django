# Generated by Django 3.0.4 on 2020-04-13 03:29

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('country', django_countries.fields.CountryField(default='MX', max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=250, verbose_name='Address line 1')),
                ('address2', models.CharField(max_length=250, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.City')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, null=True, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.City')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]