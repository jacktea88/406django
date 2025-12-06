from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()
    def __str__(self):
        return self.name
    
class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, default='超值優惠', verbose_name='手機名稱')
    description = models.TextField(default='暫無說明', verbose_name='手機說明')
    year = models.PositiveIntegerField(default=2020, verbose_name='出廠年份')
    price = models.PositiveIntegerField(default=0, verbose_name='售價')
    def __str__(self):
        return self.nickname

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='產品照片')
    url = models.URLField()
    media = models.CharField(max_length=100, default='', verbose_name='圖片檔名')
    def __str__(self):
        return self.description