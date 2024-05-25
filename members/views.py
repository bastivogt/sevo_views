from typing import Any
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models
from . import forms

# Create your views here.

# MemberListView
class MemberListView(ListView):
    model = models.Member
    context_object_name = "members"
    template_name = "members/member_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All members"
        return context
    

# MemberDetailView
class MemberDetaiView(DetailView):
    model = models.Member
    context_object_name = "member"
    template_name = "members/member_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Member detail"
        return context


# MemberCreateView
class MemberCreateView(CreateView):
    model = models.Member
    form_class = forms.MemberForm
    template_name_suffix = "_create_update_form"
    #success_url = "/members"

    def get_success_url(self):
        return reverse("member-index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create a new member"
        context["submit_label"] = "Create"
        return context
    

# MemberUpdateView
class MemberUpdateView(UpdateView):
    model = models.Member
    form_class = forms.MemberForm
    template_name_suffix = "_create_update_form"

    def get_success_url(self):
        return reverse("member-index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit a member"
        context["submit_label"] = "Edit"
        return context
    

# MemberDeleteView
class MemberDeleteView(DeleteView):
    model = models.Member
    template_name = "members/member-delete.html"
    context_object_name = "member"

    
    def get_success_url(self):
       return reverse("member-index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete member"
        return context