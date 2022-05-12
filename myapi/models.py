from django.db import models


class Representative(models.Model):
    title = models.CharField(max_length=45)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=45)
    class Meta:
        verbose_name = 'Представитель'
        verbose_name_plural = 'Представители'

    def __str__(self):
        return f'{self.title}'

class Supply(models.Model):
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE, )
    date_sup = models.DateTimeField()

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

    def __str__(self):
        return f'{self.representative}'


class Equipment(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, )
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, )
    date_order = models.DateTimeField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.equipment}'
