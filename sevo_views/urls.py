from django.urls import path

from . import views
from .sevo_class_views import v

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"), 
    path("person/<int:id>", views.PersonDetailView.as_view(), name="person-detail"),
    #path("create-person", views.create_person, name="person-create"),
    path("create-person", views.PersonCreateView.as_view(), name="person-create"),
]