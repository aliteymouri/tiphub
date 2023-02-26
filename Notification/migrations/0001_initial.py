# Generated by Django 4.1.3 on 2023-02-26 14:39

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
            name='PersonalNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='متن اعلان')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال در ')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='فرستنده')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='گیرنده')),
            ],
            options={
                'verbose_name': 'اعلان خصوصی',
                'verbose_name_plural': 'اعلان های خصوصی',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='GeneralNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='متن اعلان')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال در ')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='فرستنده')),
                ('user', models.ManyToManyField(related_name='message', to=settings.AUTH_USER_MODEL, verbose_name='گیرنده')),
            ],
            options={
                'verbose_name': 'اعلان عمومی',
                'verbose_name_plural': 'اعلان های عمومی',
                'ordering': ('-created_at',),
            },
        ),
    ]
