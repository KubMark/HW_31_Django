import json

from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.core.paginator import Paginator
from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer


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
            if field.name == 'image':
                data[field.name] = getattr(value.image, 'url', None)
            else:
                data[field.name] = getattr(value, field.name)
        result.append(data)
    return result


def index(request):
    return JsonResponse({"status": "ok"})


class AdViewSet(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.order_by("-price")



# class AdListView(generic.ListView):
#     model = Ad
#     queryset = Ad.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         self.object_list = self.object_list.select_related('author').order_by('price')
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         ads = serialize(Ad, page_obj)
#
#         response = {
#             'items': ads,
#             'num_pages': page_obj.paginator.num_pages,
#             'total': page_obj.paginator.count
#         }
#
#         return JsonResponse(
#             response,
#             safe=False
#         )


# class AdDetailView(generic.DetailView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         ad = self.get_object()
#
#         return JsonResponse({
#             "id": ad.id,
#             "name": ad.name,
#             "price": ad.price,
#             "description": ad.description,
#             "is_published": ad.is_published,
#             "image": ad.image.url,
#             "category": ad.category_id,
#             "author": ad.author_id,
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class AdCreateView(generic.CreateView):
#     model = Ad
#     fields = ["name", "price", "description", "is_published", "image", "category", "author"]
#
#     def post(self, request, *args, **kwargs):
#         ad_data = json.loads(request.body)
#
#         ad = Ad.objects.create(
#             name=ad_data["name"],
#             price=ad_data["price"],
#             description=ad_data["description"],
#             is_published=ad_data["is_published"],
#             category_id=ad_data["category_id"] if ad_data["category_id"] else None
#         )
#
#         return JsonResponse({
#             "id": ad.id,
#             "name": ad.name,
#             "price": ad.price,
#             "description": ad.description,
#             "image": ad.image.url if ad.image else None,
#             "is_published": ad.is_published,
#             "category_id": ad.category_id,
#             "author_id": ad.author_id,
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdUpdateView(generic.UpdateView):
#     model = Ad
#     fields = ["name", "price", "description", "category"]
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         ad_data = json.loads(request.body)
#         self.object.name = ad_data["name"]
#         self.object.price = ad_data["price"]
#         self.object.description = ad_data["description"]
#         # self.object.category_id = ad_data["category_id"]
#
#         self.object.save()
#
#         return JsonResponse({
#             "name": self.object.name,
#             "price": self.object.price,
#             "description": self.object.description,
#             "is_published": self.object.is_published,
#             # "category_id": self.object.category_id,
#             "author_id": self.object.author_id,
#             "image": self.object.image.url if self.object.image else None
#         })


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(generic.UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get('image')
        self.object.save()

        result = serialize(self.model, self.object)

        return JsonResponse(result, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
# class AdDeleteView(generic.DeleteView):
#     model = Ad
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'status': 'ok'}, status=200)
