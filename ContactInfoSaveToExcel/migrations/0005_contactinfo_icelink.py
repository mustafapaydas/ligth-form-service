# Generated by Django 4.0.2 on 2022-02-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactInfoSaveToExcel', '0004_contactinfo_uniqueid_contactinfo_validitytime'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='iceLink',
            field=models.CharField(max_length=200, null=True, verbose_name='Link Eki'),
        ),
    ]