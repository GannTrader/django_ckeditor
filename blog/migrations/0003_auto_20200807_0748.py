# Generated by Django 3.0.8 on 2020-08-07 07:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]