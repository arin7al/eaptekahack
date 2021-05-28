from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('ORDER_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRODUCT_ID', models.CharField(max_length=200)),
                ('QANTITY', models.FloatField),
                ('PRICE', models.FloatField),
                ('DETAIL_PAGE_URL', models.CharField(max_length=200)),
            ],
        )
#etc
    ]