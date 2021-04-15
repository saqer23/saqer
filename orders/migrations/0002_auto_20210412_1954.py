# Generated by Django 3.0.6 on 2021-04-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'OrderItem', 'verbose_name_plural': 'OrderItems'},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='Order',
        ),
    ]