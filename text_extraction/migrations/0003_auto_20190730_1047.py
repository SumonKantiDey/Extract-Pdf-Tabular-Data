# Generated by Django 2.2.3 on 2019-07-30 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text_extraction', '0002_auto_20190730_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_extraction.UserEmail', verbose_name='User Name'),
        ),
    ]
