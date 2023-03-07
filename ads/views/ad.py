from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer, AdDetailSerializer, AdListSerializer


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
    default_serializer = AdSerializer
    queryset = Ad.objects.order_by("-price")
    serializers = {"retrieve": AdDetailSerializer,
                   "list": AdListSerializer}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)
        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


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

