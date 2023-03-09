from rest_framework.routers import SimpleRouter
from ads.views.ad import AdViewSet

router = SimpleRouter()
router.register("", AdViewSet)
urlpatterns = router.urls
