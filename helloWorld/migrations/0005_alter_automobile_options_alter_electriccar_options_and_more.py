# Generated by Django 4.2.2 on 2023-08-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0004_alter_automobile_id_alter_electriccar_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobile',
            options={'verbose_name': 'Automobile', 'verbose_name_plural': 'Automobiles'},
        ),
        migrations.AlterModelOptions(
            name='electriccar',
            options={'verbose_name': 'Electric Car', 'verbose_name_plural': 'Electric Cars'},
        ),
        migrations.AlterModelOptions(
            name='icecar',
            options={'verbose_name': 'I.C.E. Car', 'verbose_name_plural': 'I.C.E. Cars'},
        ),
        migrations.AddField(
            model_name='automobile',
            name='range',
            field=models.FloatField(default=1),
        ),
    ]
