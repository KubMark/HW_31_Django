import factory.django
from ads.models import Ad, Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)

class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker("name")
    price = 200
    description = ""
    author = factory.SubFactory(UserFactory)

