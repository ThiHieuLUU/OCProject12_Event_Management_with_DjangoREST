# Generated by Django 3.2.5 on 2021-08-02 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_official_client', models.BooleanField(default=False)),
                ('main_sales_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_signed', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='events.client')),
                ('sales_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contract',
                'verbose_name_plural': 'contracts',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='event', serialize=False, to='events.contract')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('CANCELED', 'Canceled'), ('IN PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='SCHEDULED', max_length=25)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('support_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]