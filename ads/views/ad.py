from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from ads.models import Ad, Selection
from ads.permissions import IsOwner, IsStaff
from ads.serializers import AdSerializer, AdDetailSerializer, AdListSerializer, SelectionSerializer, \
    SelectionCreateSerializer


def index(request):
    return JsonResponse({"status": "ok"})


class AdViewSet(ModelViewSet):
    default_serializer = AdSerializer
    queryset = Ad.objects.order_by("-price")
    serializers = {"retrieve": AdDetailSerializer,
                   "list": AdListSerializer,
                   }

    default_permission = [AllowAny]
    permissions = {"retrieve": [IsAuthenticated],
                   "update": [IsAuthenticated, IsOwner | IsStaff],
                   "partial_update": [IsAuthenticated, IsOwner | IsStaff],
                   "destroy": [IsAuthenticated, IsOwner | IsStaff]
                   }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

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


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_permission = [AllowAny]
    permissions = {"create": [IsAuthenticated],
                   "retrieve": [AllowAny],
                   "list": [AllowAny],
                   "update": [IsAuthenticated, IsOwner],
                   "partial_update": [IsAuthenticated, IsOwner],
                   "destroy": [IsAuthenticated, IsOwner]}

    default_serializer = SelectionSerializer
    serializers = {"create": SelectionCreateSerializer,
                   }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
