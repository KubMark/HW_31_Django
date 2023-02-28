from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views.ad import *

router = SimpleRouter()
router.register("", AdViewSet)

urlpatterns = [
    # path('<int:pk>/', AdDetailView.as_view()),
    # path('create/', AdCreateView.as_view(), name='ad_create'),
    # path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    # path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('<int:pk>/image/', AdImageView.as_view(), name='ad_image'),

]

urlpatterns += router.urls
