from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nombre>", views.saludar, name="saludar"),
    path("olivo", views.olivo, name="olivo"),

]