from django.db import models


# Create your models here.

class Basket(models.Model):
    ORDER_ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    PRODUCT_ID = models.CharField(max_length=200)
    QANTITY = models.FloatField
    PRICE = models.FloatField
    DETAIL_PAGE_URL = models.CharField(max_length=200)

# class Orders(models.Model):
 #    "ID": 12076390,
 #    "PERSON_TYPE_ID": 1,
 #    "DATE_INSERT": "2021-03-11 22:06:59",
 #    "STATUS_ID": "F",
 #    "LID": "s1",
 #    "USER_ID": 44
 #  },


 # Products
 # # {
 # #     "ID": 461363,
 # #     "NAME": "Виагра, таблетки 100 мг, 2 шт."
 # # },
 #

 # Property ???
 # # {
 # #     "ID": 276,
 # #     "CODE": "ALSO_BUY",
 # #     "NAME": "С этим товаром также покупают"
 # # },
 #

 # propertyMultipleValues.json
 # # {
 # #     "IBLOCK_ELEMENT_ID": 461363,
 # #     "IBLOCK_PROPERTY_ID": "356",
 # #     "VALUE": "6817",
 # #     "VALUE_ENUM": null,
 # #     "VALUE_NUM": 6817.0000,
 # #     "DESCRIPTION": null
 # # },
 #

 # propertyValues.json
 # # {
 # #     "IBLOCK_ELEMENT_ID": 461363,
 # #     "PROPERTY_276": "a:3:{s:5:\"VALUE\";a:0:{}s:11:\"DESCRIPTION\";a:0:{}s:2:\"ID\";a:0:{}}",
 # #     "PROPERTY_429": "a:3:{s:5:\"VALUE\";a:0:{}s:11:\"DESCRIPTION\";a:0:{}s:2:\"ID\";a:0:{}}",
 # #     "PROPERTY_326": "23a5c4b5-6f26-4053-b728-cb864a4edcbd",
 # #     "PROPERTY_574": "66",
 # #     "PROPERTY_265": "США",
 # #     "PROPERTY_284": null,
 # #     "PROPERTY_541": "100 мг",
 # #     "PROPERTY_542": "таблетки",
 # #     "PROPERTY_343": "100177",
 # #     "PROPERTY_428": "tabletki",
 # #     "PROPERTY_274": "таблетки 100 мг, 2 шт.",
 # #     "PROPERTY_263": 1.0000,
 # #     "PROPERTY_264": "Пфайзер",
 # #     "PROPERTY_594": "",
 # #     "PROPERTY_344": "a219a283-5674-498e-a828-d11bd7d7c4fc",
 # #     "PROPERTY_483": 0.0000,
 # #     "PROPERTY_536": "drug",
 # #     "PROPERTY_540": "2",
 # #     "PROPERTY_356": "a:3:{s:5:\"VALUE\";a:2:{i:0;s:4:\"6817\";i:1;s:4:\"9528\";}s:11:\"DESCRIPTION\";a:2:{i:0;N;i:1;N;}s:2:\"ID\";a:2:{i:0;s:7:\"6557061\";i:1;s:7:\"6557062\";}}",
 # #     "PROPERTY_567": "a:3:{s:5:\"VALUE\";a:0:{}s:11:\"DESCRIPTION\";a:0:{}s:2:\"ID\";a:0:{}}",
 # #     "PROPERTY_332": "RX",
 # #     "PROPERTY_283": ""
 # # },