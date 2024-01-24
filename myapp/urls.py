from django.urls import path, re_path
from myapp import views

from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     path('department', views.departmentApi),
#     re_path(r'^department/([0-9]+)$', views.departmentApi),

#     path('employee', views.employeeApi),
#     re_path(r'^employee/([0-9]+)$', views.employeeApi),

#     path('employee/savefile', views.SaveFile),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailViewSet

router = DefaultRouter()
#router.register(r'email', EmailViewSet.as_view(), basename='email')

urlpatterns = [
    #path('', include(router.urls)),
    path('email/', EmailViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

