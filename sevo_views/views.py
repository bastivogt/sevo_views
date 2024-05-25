from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from .sevo_class_views import v

from . import models
from . import forms

# Create your views here.



# list
class IndexListView(v.ListView):
    model = models.Person
    template_name = "sevo_views/index.html"

    def get_context(self):
        context =  super().get_context()
        context["title"] = "All People"
        return context
    
    def get_queryset(self):
        return super().get_queryset().order_by("firstname")
    
    def get_queries(self):
        q = self.get_query_object()
        #q = q.filter(lastname="Vogt").order_by("-birthday")
        q = q.order_by("birthday")
        return q



# read
class PersonDetailView(v.DetailView):
    model = models.Person
    template_name = "sevo_views/person_detail.html"
    context_model_name = "person"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Person detail"
        return context


# create
class PersonCreateView(v.CreateUpdateView):
    model_form = forms.PersonForm
    template_name = "sevo_views/create_update_person.html"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Create new person"
        context["submit_label"] = "Create"
        return context

    def success(self, request, **kwargs):
        print("success")
        url = reverse("people-index")
        return HttpResponseRedirect(url)
        

# update
class PersonUpdateView(v.CreateUpdateView):
    model_form = forms.PersonForm
    model = models.Person
    template_name = "sevo_views/create_update_person.html"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Create new person"
        context["submit_label"] = "Update"
        return context

    def success(self, request, **kwargs):
        print("success")
        url = reverse("people-index")
        return HttpResponseRedirect(url)



# delete
class PersonDeleteView(v.DeleteView):
    template_name = "sevo_views/person_delete.html"
    model = models.Person
    redirect_path_name = "people-index"