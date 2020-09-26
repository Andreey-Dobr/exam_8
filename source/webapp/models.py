from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


CATEGORY_CHOICES = [
    ('services', 'услуги'),
    ('products', 'товары'),
    ('relaxation', 'отдых'),
    ('no_category', 'без категории')
]

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=100,verbose_name='категория',choices=CATEGORY_CHOICES, null=False, blank=False,
                            default='no_category')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='картинка')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='reviews',
                                on_delete=models.CASCADE, verbose_name='Продукт')
    text = models.TextField(max_length=400,null=False, verbose_name='Комментарий')
    appraisal = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], null=False,
                                    verbose_name='Оценка')


    def __str__(self):
        return self.text[:20]