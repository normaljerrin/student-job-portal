# Generated by Django 4.1.7 on 2023-03-19 11:45

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
            name='application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, upload_to='image/')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('college', models.CharField(blank=True, max_length=200)),
                ('qualification', models.CharField(blank=True, choices=[('Master', 'Master'), ('Btech', 'Btech'), ('Degree', 'Degree'), ('Diploma', 'Diploma'), ('Other', 'Other')], default='qualification', max_length=200)),
                ('company', models.CharField(blank=True, choices=[('TCS', 'TCS'), ('IBM', 'IBM'), ('Wipro', 'Wipro'), ('Facebook', 'Facebook'), ('Microsoft', 'Microsoft'), ('Google', 'Google'), ('Tesla', 'Tesla'), ('Honda', 'Honda')], default='company', max_length=200)),
                ('skill', models.TextField(blank=True, max_length=200)),
                ('resume', models.FileField(blank=True, max_length=200, upload_to='resume/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]