from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    class Paymentmethod(models.TextChoices):
        CASH = 'cash'
        TRANSFER = 'transfer'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment', verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment', verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment', verbose_name='Оплаченный урок', **NULLABLE)
    amount_payment = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=25, verbose_name='Способ оплаты', choices=Paymentmethod.choices)

    def __str__(self):
        return f'{self.user} - {self.amount_payment} - {self.payment_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-payment_date',)
