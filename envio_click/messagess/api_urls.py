from rest_framework.routers import DefaultRouter
from messagess import views

router = DefaultRouter()
router.register('messagess', views.MessageViewSet)

urlpatterns = router.urls