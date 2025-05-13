from django.urls import path, include
from rest_framework import routers
from snippets import views


router = routers.DefaultRouter()
router.register(r'sn', views.SnippetViewSet)

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets-viewset/', include(router.urls)),
]