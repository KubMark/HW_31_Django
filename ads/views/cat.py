import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from ads.models import Category


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


class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.all()


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')

        categories = self.queryset
        cat_list = serialize(Category, categories)
        return JsonResponse(cat_list, safe=False)


class CategoryDetailView(generic.DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.pk, "name": category.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        new_cat = Category.objects.create(**ad_data)
        result = serialize(Category, new_cat)
        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        new_cat = Category.objects.get(id=kwargs['pk'])
        new_cat.name = ad_data['name']
        new_cat.save()

        result = serialize(Category, new_cat)
        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=200)
