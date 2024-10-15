# Generated by Django 3.2.4 on 2021-06-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='approval',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=15),
        ),
    ]
