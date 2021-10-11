# Generated by Django 3.2.8 on 2021-10-09 18:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bandwidth', '0003_alter_upgrade_upgrade_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='upgrade',
            name='upgrade_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bandwidth.author'),
            preserve_default=False,
        ),
    ]