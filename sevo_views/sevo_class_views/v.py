from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# BaseView
class BaseView():

    template_name = "base_test.html"
    _instance = None


    @classmethod
    def as_view(cls, **kwargs):
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


# View
class View(BaseView):

    def get(self, request, **kwargs):
        return render(request, type(self).template_name, type(self)._instance.get_context())


    def post(self, request, **kwargs):
        pass

    def _setup(self, request, **kwargs):
        ret = None
        if request.method == "POST":
            return self.post(request, **kwargs)

        return self.get(request, **kwargs)

        # if request.method == "GET":
        #     ret =  self.get(request, **kwargs)


        # if ret != None:
        #     return ret
        
        # return super()._setup(request, **kwargs)

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
        

class CreateView(View):
    model_form: None
    context_model_form_name = "form"
    form_object = None

    def get_context(self):
        context = super().get_context()
        context[type(self).context_model_form_name] = type(self).form_object
        return context


    def success(self, request, **kwargs):
        return super()._setup(request, **kwargs)

    def fail(self, request, **kwargs):
        return super()._setup(request, **kwargs)

    def post(self, request, **kwargs):
        type(self).form_object = type(self).model_form(request.POST)
        if type(self).form_object.is_valid():
            type(self).form_object.save()
            return self.success(request, **kwargs)
        return self.fail(request, **kwargs)
        


    def get(self, request, **kwargs):
        type(self).form_object = type(self).model_form()
        return super().get(request, **kwargs)



