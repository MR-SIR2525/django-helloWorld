from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0005_alter_automobile_options_alter_electriccar_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobile',
            name='displacement',
            field=models.FloatField(default=0.1),
        ),
    ]