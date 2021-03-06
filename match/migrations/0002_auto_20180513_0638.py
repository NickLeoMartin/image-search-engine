# Generated by Django 2.0.5 on 2018-05-13 06:38

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_features',
            field=picklefield.fields.PickledObjectField(default=None, editable=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_file',
            field=models.ImageField(upload_to='img'),
        ),
    ]
