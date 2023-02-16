from django.db import models

# "name": "Молодая кошечка Груша",
# "author": "Галина",
# "price": 100,
# "description": "Груша - сладкая, яркая и очень милая кошка! Предпочитает держаться отстраненно, но мы уверены, что в жизни каждой пугливой кошки рано или поздно появляется человек, которому они будут доверять. Давайте поможем ей найти такого человека! Отдается под договор с ненавязчивым отслеживанием.",
# "address": "Москва, м. Черкизовская",
# "is_published": true
class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=300)
    is_published = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)