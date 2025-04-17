from django.contrib import admin
from django.urls import path
from property import views

urlpatterns = [
    path('', views.show_flats),
    path('search/', views.show_flats),
    path('admin/', admin.site.urls),
]
