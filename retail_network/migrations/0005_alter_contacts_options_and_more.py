# Generated by Django 4.2.4 on 2023-09-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail_network', '0004_alter_basenetobject_arrears_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['city'], 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='house',
            new_name='house_number',
        ),
        migrations.AlterField(
            model_name='entrepreneur',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retail_network.retailer'),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retail_network.factory'),
        ),
    ]
