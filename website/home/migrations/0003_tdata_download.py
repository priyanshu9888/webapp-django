# Generated by Django 3.2.8 on 2021-12-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tdata',
            name='download',
            field=models.FileField(default='', upload_to='files/'),
            preserve_default=False,
        ),
    ]
