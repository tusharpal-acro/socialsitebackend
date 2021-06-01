from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register('postlike-view-set',views.PostLikeViewSet,basename='postlike-view-set')
router.register('user-view-set',views.UserViewSet,basename='user-view-set')

urlpatterns = [
    path('', include(router.urls)),
    url(r'posts/(?P<pk>\d+)/$', view=views.PostViewSet.as_view({'get':'post', 'post':'post'})),
    path('login/', views.LoginApi.as_view(), name='login'),
]