from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# BaseView
class BaseView():

    template_name = "base_test.html"
    _instance = None


    @classmethod
    def as_view(cls, **init_kwargs):
        for key in init_kwargs:
            if hasattr(cls, key):
                setattr(cls, key, init_kwargs[key])

        
        def view_function(request, **kwargs):
            cls._instance = cls()
            setup_return = cls._instance._setup(request, **kwargs)
            cls._instance.after_setup(request, **kwargs)
            return setup_return
        return view_function
        

    def get_context(self):
        return {}
    
    def _setup(self, request, **kwargs):
        return render(request, type(self).template_name, type(self)._instance.get_context())


    def after_setup(self, request, **kwargs):
        pass

# RedirectView
class RedirectView(BaseView):
    path_name = None

    def _setup(self, request, **kwargs):
        if type(self).path_name == None:
            raise Exception("path_name must be not None")
        url = reverse(type(self).path_name)
        return HttpResponseRedirect(url)



# View
class View(BaseView):

    def get(self, request, **kwargs):
        return render(request, type(self).template_name, type(self)._instance.get_context())


    def post(self, request, **kwargs):
        pass

    def _setup(self, request, **kwargs):
        if request.method == "POST":
            return self.post(request, **kwargs)

        return self.get(request, **kwargs)



# ListView
class ListView(BaseView):
    model = None
    context_model_name = "model"
    _query_object = None

    def get_context(self):
        context = super().get_context()
        context[type(self).context_model_name] = type(self)._query_object
        return context

    def get_query_object(self):
        return type(self)._query_object
    

    def get_queryset(self):
        return type(self).model.objects.all()
    

    def get_queries(self):
        return self.get_query_object()

    def _setup(self, request, **kwargs):
        type(self)._query_object = self.get_queryset()
        type(self)._query_object = self.get_queries()
        return super()._setup(request, **kwargs)



# DetailView
class DetailView(BaseView):
    model = None
    context_model_name = "model"
    query_object = None

    def get_context(self):
        context = super().get_context()
        context[type(self).context_model_name] = type(self).query_object
        return context
    
    def _setup(self, request, **kwargs):
        type(self).query_object = get_object_or_404(type(self).model, **kwargs)
        return super()._setup(request, **kwargs)
        



class CreateUpdateView(View):
    model_form: None
    model = None
    context_model_form_name = "form"
    _form_instance = None
    _model_instance = None

    def get_context(self):
        context = super().get_context()
        context[type(self).context_model_form_name] = type(self)._form_instance
        return context


    def success(self, request, **kwargs):
        return self.get(request, **kwargs)


    def fail(self, request, **kwargs):
        return self.get(request, **kwargs)

    def post(self, request, **kwargs):
        if type(self).model:
            type(self)._form_instance = type(self).model_form(request.POST, instance=type(self)._model_instance)
        else:
            type(self)._form_instance = type(self).model_form(request.POST)
        
        if type(self)._form_instance.is_valid():
            type(self)._form_instance.save()
            return self.success(request, **kwargs)
        return self.fail(request, **kwargs)
        


    def _setup(self, request, **kwargs):
        if type(self).model:
            type(self)._model_instance = get_object_or_404(type(self).model, **kwargs)
        return super()._setup(request, **kwargs)
    
    def get(self, request, **kwargs):
        if type(self).model:
            type(self)._form_instance = type(self).model_form(instance=type(self)._model_instance)
        else:
            type(self)._form_instance = type(self).model_form()
        return super().get(request, **kwargs)



# DeleteView
class DeleteView(View):
    model = None
    _model_instance = None
    context_model_name = "model"
    redirect_path_name = None

    def _setup(self, request, **kwargs):
        type(self)._model_instance = get_object_or_404(type(self).model, **kwargs)
        return super()._setup(request, **kwargs)
    

    def get_context(self):
        context = super().get_context()
        context[type(self).context_model_name] = type(self)._model_instance
        return context
    
    def success(self, request, **kwargs):
        pass

    def post(self, request, **kwargs):
        type(self)._model_instance.delete()
        self.success(request, **kwargs)
        url = reverse(type(self).redirect_path_name)
        return HttpResponseRedirect(url)
        
