# Generated by Django 2.2.3 on 2019-07-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destapacionesposta', '0005_auto_20190621_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos_register',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
