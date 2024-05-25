from django.urls import path

from . import views


urlpatterns = [
    path("", views.MemberListView.as_view(), name="member-index"),
    path("member-detail/<int:pk>", views.MemberDetaiView.as_view(), name="member-detail"),
    path("member-create", views.MemberCreateView.as_view(), name="member-create"),
    path("member-update/<int:pk>", views.MemberUpdateView.as_view(), name="member-update"),
    path("member-delete/<int:pk>", views.MemberDeleteView.as_view(), name="member-delete")

]