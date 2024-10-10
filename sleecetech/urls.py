from django.db import router
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register('messages', views.SleeceMessageViewSet)

urlpatterns = router.urls