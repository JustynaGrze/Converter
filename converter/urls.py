from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:converter_id>', views.converter, name='converter'),
    path('<int:converter_id>/convert', views.convert, name='convert'),

]