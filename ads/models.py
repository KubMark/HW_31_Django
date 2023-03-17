from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], unique=True)


class Ad(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])#Валидатор на мин длину
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)


class Selection(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name



