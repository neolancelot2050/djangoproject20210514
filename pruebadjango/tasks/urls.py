from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add",views.add, name="add")
    #path("<str:nombre>", views.saludar, name="saludar"),
    #path("olivo", views.olivo, name="olivo"),

]