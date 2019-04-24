from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from instawork.views import UserViewSet

schema_view = get_swagger_view(title='TeamMember API')

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^swagger/$', schema_view),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
