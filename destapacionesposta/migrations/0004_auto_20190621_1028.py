# Generated by Django 2.2.2 on 2019-06-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destapacionesposta', '0003_auto_20190621_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administracion',
            name='mail',
            field=models.EmailField(max_length=50),
        ),
    ]