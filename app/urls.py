from rest_framework.routers import DefaultRouter
from .views import TaskViewSet


router = DefaultRouter()

router.register("jobs", TaskViewSet)

urlpatterns = router.urls