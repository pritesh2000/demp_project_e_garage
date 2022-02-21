# Generated by Django 4.0.2 on 2022-02-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_customer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('STATUS', models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('completed', 'completed')], max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.product')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
