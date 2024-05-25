from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from .sevo_class_views import v

from . import models
from . import forms

# Create your views here.


class IndexView(v.BaseView):
    template_name = "sevo_views/index.html"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Hello world, from index.html!"
        return context
    

class IndexView2(v.View):
    template_name = "sevo_views/index.html"

    def get(self, request, **kwargs):
        print("Hello from get")
        print(request.user)


    def get_context(self):
        context = super().get_context()
        context["title"] = "Hello world 2!"
        return context


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
        q = q.filter(lastname="Vogt").order_by("-birthday")
        return q




class PersonDetailView(v.DetailView):
    model = models.Person
    template_name = "sevo_views/person_detail.html"
    context_model_name = "person"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Person detail"
        return context



class PersonCreateView(v.CreateUpdateView):
    model_form = forms.PersonForm
    template_name = "sevo_views/create_update_person.html"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Create new person"
        return context

    def success(self, request, **kwargs):
        print("success")
        url = reverse("index")
        return HttpResponseRedirect(url)
        


class PersonUpdateView(v.CreateUpdateView):
    model_form = forms.PersonForm
    model = models.Person
    template_name = "sevo_views/create_update_person.html"

    def get_context(self):
        context = super().get_context()
        context["title"] = "Create new person"
        return context

    def success(self, request, **kwargs):
        print("success")
        url = reverse("index")
        return HttpResponseRedirect(url)



def index(request):
    v.BaseView.as_view()
    v.View.as_view()
    return render(request, "sevo_views/index.html", {
        "title": "all people"
    })


def create_person(request):
    if request.method == "POST":
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
    else:
        form = forms.PersonForm()

    return render(request, "sevo_views/create_person.html", {
        "title": "CREATE PERSON",
        "form": form
    })