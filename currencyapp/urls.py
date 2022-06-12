
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('dolar/',views.dolar,name="dolar"),
    path('euro/',views.euro,name="euro"),
    path('gbp/', views.gbp, name="gbp"),
]
