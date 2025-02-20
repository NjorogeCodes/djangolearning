# Generated by Django 5.1.2 on 2024-11-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_cat', models.CharField(max_length=100)),
                ('prod_price', models.FloatField()),
                ('prod_qty', models.IntegerField()),
                ('prod_img', models.ImageField(default='default.jpg', upload_to='products/')),
                ('prod_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
