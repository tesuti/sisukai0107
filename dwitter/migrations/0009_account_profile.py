# Generated by Django 4.1.5 on 2023-01-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0008_alter_account_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='dwitter.profile'),
            preserve_default=False,
        ),
    ]
