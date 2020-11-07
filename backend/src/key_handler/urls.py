from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('update_session', views.update_session),
    path('list_sessions', views.list_sessions),
]

urlpatterns = format_suffix_patterns(urlpatterns)

