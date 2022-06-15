from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexView,name='home'),
    path('dashboard/',views.dashboardViews,name='dashboard'),
    path('login/',),
    path('register/',),
    path('logout/',),
]
