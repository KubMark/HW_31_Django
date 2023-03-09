from rest_framework.routers import SimpleRouter
from ads.views.ad import SelectionViewSet

router = SimpleRouter()
router.register("", SelectionViewSet)
urlpatterns = router.urls
