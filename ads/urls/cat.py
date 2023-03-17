from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views.cat import CatViewSet

# from ads.views.cat import *

# urlpatterns = [
#     path('', CategoryListView.as_view(), name='category_list'),
#     path('create/', CategoryCreateView.as_view(), name='category_create'),
#     path('<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
#     path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
#     path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
#
# ]

cat_router = SimpleRouter()
cat_router.register("", CatViewSet)
urlpatterns = cat_router.urls
