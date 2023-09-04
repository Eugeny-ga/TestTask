from django.db import models

class Contacts(models.Model):
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=50, verbose_name='Дом')

    def __str__(self):
        return self.city + ', ' + self.street

    class Meta:
        ordering = ["city"]
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



class BaseNetObject(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.PROTECT, verbose_name='Контакты')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    arrears = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Задолженность')
    date_created = models.DateField(auto_now_add=True, editable=False, verbose_name='Дата создания')

    def __str__(self):
        return self.title

class Factory(BaseNetObject):

    class Meta:
        verbose_name_plural = 'Заводы'
        verbose_name = 'Завод'
        ordering = ["title"]


class Retailer(BaseNetObject):
    provider = models.ForeignKey(Factory, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Розничные сети'
        verbose_name = 'Розничная сеть'
        ordering = ["title"]


class Entrepreneur(BaseNetObject):
    provider = models.ForeignKey(Retailer, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Предприниматели'
        verbose_name = 'Предприниматель'
        ordering = ["title"]


