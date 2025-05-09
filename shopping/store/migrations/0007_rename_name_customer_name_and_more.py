# Generated by Django 5.1.1 on 2024-10-21 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
