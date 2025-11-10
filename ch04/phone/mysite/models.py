from django.db import models

# Create your models here.
class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True, )
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now=True, )
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()

# auto_now 會在每次保存模型時，將日期字段設置為目前的日期和時間。
# auto_now_add 會在模型第一次創建時，將日期字段設置為目前的日期和時間，並且在後續更新時不會變更。

class Product(models.Model):
    SIZES = (
        ('S', 'Smaill'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.IntegerField(default=0)