# Generated by Django 4.2.5 on 2023-12-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0002_remove_invoice_uuid_invoice_note_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoicehistory",
            name="invoice_date",
            field=models.DateTimeField(),
        ),
    ]
