# Generated by Django 2.2.3 on 2019-08-22 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_extraction', '0014_braemarspotassesment_braemarspotfixture_braemartimeassesment1_braemartimeassesment2_braemartimefixtu'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='braemarspotassesment',
            table='braemarspotassesment',
        ),
        migrations.AlterModelTable(
            name='braemarspotfixture',
            table='braemarspotfixture',
        ),
        migrations.AlterModelTable(
            name='braemartimeassesment1',
            table='braemartimeassesment1',
        ),
        migrations.AlterModelTable(
            name='braemartimeassesment2',
            table='braemartimeassesment2',
        ),
        migrations.AlterModelTable(
            name='braemartimefixture',
            table='braemartimefixture',
        ),
    ]
