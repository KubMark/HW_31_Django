import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


def serialize(model, values):
    if isinstance(values, model):
        values = [values]
    else:
        list(values)

    result = []

    for value in values:
        data = {}
        for field in model._meta.get_fields():
            if field.is_relation:
                continue
            data[field.name] = getattr(value, field.name)
        result.append(data)
    return result


class CatViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()