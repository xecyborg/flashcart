# Generated by Django 5.1.2 on 2024-10-30 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]
