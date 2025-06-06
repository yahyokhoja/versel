# Generated by Django 5.2 on 2025-05-22 04:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_created_at_storeownerprofile_additional_info_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='storeownerprofile',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner_profile', to='store.store'),
        ),
        migrations.AlterField(
            model_name='storeownerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store_owner_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
