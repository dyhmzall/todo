from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from project.views import ProjectModelViewSet, TodoModelViewSet
from project.views import ProjectAPIView
from project.views import ProjectRetrieveAPIView
from project.views import ProjectViewSet
from project.views import ProjectKwargsFilterView
from project.views import ProjectParamFilterViewSet
from project.views import ProjectDjangoFilterViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)
# router.register('base', ProjectViewSet, basename='project')

# filter_router = DefaultRouter()
# filter_router.register('param', ProjectParamFilterViewSet)
#
# django_fitler_router = DefaultRouter()
# django_fitler_router.register('best', ProjectDjangoFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('views/api-view/', ProjectAPIView.as_view()),
    # path('generic/retrieve/<str:pk>/', ProjectRetrieveAPIView.as_view()),
    # path('viewsets', include(router.urls)),
    # filtering
    # path('filters/kwargs/<str:name>/', ProjectKwargsFilterView.as_view()),
    # path('param/filter/', include(filter_router.urls)),
    # django-filter
    # path('best/filter/', include(django_fitler_router.urls)),
]
