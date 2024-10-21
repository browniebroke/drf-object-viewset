from rest_framework.routers import DefaultRouter

from app1.views import ObjectViewSet

router = DefaultRouter()
router.register(r"objects", ObjectViewSet, basename="object")

urlpatterns = router.urls