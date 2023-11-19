from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .models import Automobile, iceCar, ElectricCar
from .forms import addAutomobileForm, AutomobileIdForm, confirmUpdateAutomobile \
    , deleteAutomobileForm
from django.views import View
from django.views.generic import ListView, UpdateView

from django.contrib import messages #ability to send alerts to templates/pages



class Home(View):
    def get(self, request):
        # messages.info(self.request, f"This is a test")
        return render(request, 'home.html')
    

class AutomobileList(ListView):
    model = Automobile
    template_name = "singleList.html"

    # Return a list containing all fields name
    model_fields = [field.name for field in model._meta.get_fields()]
    
    # Override get_context_data() in order to pass additional context variables 
    # to the template. Adding a variable to the context; new template variable.
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views    
    def get_context_data(self, **kwargs):
        """Returns context of:  object_list, modelName, model_fields"""
        # Call the base implementation first to get the context
        context = super(AutomobileList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['modelName'] = 'Automobile'
        context['model_fields'] = self.model_fields
        return context

    
class iceCarList(ListView):
    model = iceCar
    template_name = "singleList.html"

    # Return a list containing names of all fields
    model_fields = [field.name for field in model._meta.get_fields()]
    
    # Override get_context_data() in order to pass additional context variables 
    # to the template. Adding a variable to the context; new template variable.
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(iceCarList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['modelName'] = 'internal combustion engine (ICE) car'
        context['model_fields'] = self.model_fields
        return context   


class ElectricCarList(ListView):
    model = ElectricCar
    template_name = "singleList.html"

    # Return a list containing all fields name
    model_fields = [field.name for field in model._meta.get_fields()]
    
    # Override get_context_data() in order to pass additional context variables 
    # to the template. Adding a variable to the context; new template variable.
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ElectricCarList, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['modelName'] = 'electric car'
        context['model_fields'] = self.model_fields
        return context


class AutomobileCreate(View):
    form = addAutomobileForm
    template_name = 'carAdd.html'
    context = {
        'form': form(), 
        'modelName':'automobile',
        'operation':'create'
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_entity = bound_form.save()
            messages.success(self.request, f"Successfully added {new_entity} to the database.")
            return redirect('automobile-stats')
        else:
            return render(request, self.template_name, {'form': bound_form})

class AutomobileUpdate(ListView):
    model = Automobile
    form = addAutomobileForm
    id_form = AutomobileIdForm
    confirm = confirmUpdateAutomobile
    template_name = 'carUpdate.html'
    extra_context = {
        'form': form,
        'id_form': id_form,
        'confirm': confirm,
        'operation': 'update'
    }
    model_fields = [field.name for field in model._meta.get_fields()]
    
    def get_context_data(self, **kwargs):
        context = super(AutomobileUpdate, self).get_context_data(**kwargs)

        # Determine if updating an existing Automobile
        automobile_id = self.request.POST.get('automobile_id')
        if automobile_id:
            instance = get_object_or_404(Automobile, id=automobile_id)
            context['form'] = self.form(instance=instance)  # Bind instance to the form
        else:
            context['form'] = self.form()  # New form for creation

        context['modelName'] = 'Automobile'
        context['model_fields'] = self.model_fields
        context.update(self.extra_context)
        return context

    def post(self, request, *args, **kwargs):
        automobile_id = request.POST.get('automobile_id')
        if automobile_id:
            instance = get_object_or_404(Automobile, id=automobile_id)
            form = self.form(request.POST, instance=instance)  # Update existing instance
            
            if form.is_valid():
                form.save()
                messages.success(request, f"Successfully updated Automobile: {form}.")
            else:
                messages.info(request, f"One or more things you entered were invalid.")

            return redirect('automobile-stats')
        
        else:
            messages.warning(request, f'No Automobile id given, or it was invalid.')
            form = self.form(request.POST)  # Return form as is to the user?
            return self.render_to_response(self.get_context_data())


def executeAutomobileUpdate(request, id):
    """A dependency of AutomobileUpdate view (my old version). This does the actual update.
       Redirects to the same page with either success or error message.\n
       https://www.geeksforgeeks.org/update-view-function-based-views-django/
    """
    # fetch the object related to passed id
    obj = get_object_or_404(Automobile, id=id)
    if obj == Http404:
        messages.warning(request, f'No Automobile with id {id} exists in the database.')
        return redirect('automobile-update')

    # pass the object as instance in the form
    form = addAutomobileForm(request.POST or None, instance = obj)

    # save the data from the form and redirect
    if form.is_valid():
        form.save()
        # return redirect("/"+id)
        messages.success(request, "Update successful.")
    else:
        messages.warning(request, "Could not update.")

    return redirect('automobile-update')



class AutomobileDelete(ListView):
    """Basically, AutomobileList view with a delete form attached."""
    model = Automobile
    form = deleteAutomobileForm
    template_name = 'carDelete.html'
    extra_context = {
        'form':form, 
        'modelName':'automobile',
        'operation':'delete'
    }
    model_fields = [field.name for field in model._meta.get_fields()]
    
    def get_context_data(self, **kwargs):
        """Override to insert custom context."""
        context = super(AutomobileDelete, self).get_context_data(**kwargs)
        context['model_fields'] = self.model_fields
        context.update(self.extra_context)
        return context

    def post(self, request):
        automobile_id = request.POST.get('automobile_id')
        if automobile_id:
            try:
                targetAutomobile = get_object_or_404(Automobile, pk=automobile_id)
                targetAutomobile.delete()
                messages.info(request, f"Success. Deleted Automobile of id {automobile_id}.")
                return redirect('automobile-stats')    
            except Http404:
                messages.warning(request, f"No Automobile with id of {automobile_id}")
                return redirect('automobile-delete')
        else:
            messages.warning(request, 'An error occured.')
            return redirect('automobile-delete')


class carstats(View):
    """Lists all Automobiles and IceCars and ElectricCars on one page.
       On the site, the link is 'All Three'"""
    def get(self, request):
        """Context consists of:\n
           data: a list of all objects \n
           models: model names used\n
           title: The title of the page.\n"""
        data = [
            {
                'model': Automobile, 
                'objects': Automobile.objects.all(), 
                'verbose_name_plural': Automobile._meta.verbose_name_plural,
                'fields': [f for f in Automobile._meta.get_fields() if not f.is_relation]
            },
            {
                'model': iceCar, 
                'objects': iceCar.objects.all(), 
                'verbose_name_plural': iceCar._meta.verbose_name_plural,
                'fields': [f for f in iceCar._meta.get_fields() if not f.is_relation]
            },
            {
                'model': ElectricCar, 
                'objects': ElectricCar.objects.all(), 
                'verbose_name_plural': ElectricCar._meta.verbose_name_plural,
                'fields': [f for f in ElectricCar._meta.get_fields() if not f.is_relation]
            },
        ]
        
        context = {
            'data': data,
            'models': {'Automobile', 'ICE Car', 'Electric Car'},
            'title': 'All 3 Types of Cars - Andrew\'s Django Page',
        }
        
        return render(request, 'carstats.html', context)

'''class AutomobileUpdate(ListView):
    """Just like this AutomobileList view, this renders a list of Automobile entities, but 
       includes forms and PUT request handling, forwarded to executeAutomobileUpdate view,
       to update Automobile entities.
    """
    model = Automobile
    form1 = AutomobileIdForm
    form2 = addAutomobileForm
    confirm = confirmUpdateAutomobile
    template_name = 'carUpdate.html'
    extra_context = {
        'form1':form1,
        'form2':form2,
        'confirm':confirm,
        'operation':'update'
    }
    #Don't use this for user objects. They have too many confidential fields
    model_fields = [field.name for field in model._meta.get_fields()]
    
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views    
    def get_context_data(self, **kwargs):
        """Override to insert custom context.\n
           Returns context:  object_list, modelName, model_fields, form1, form2, operation
        """
        context = super(AutomobileUpdate, self).get_context_data(**kwargs)
        context['modelName'] = 'Automobile'
        context['model_fields'] = self.model_fields
        context.update(self.extra_context)
        return context

    def post(self, request, *args, **kwargs):
        automobile_id = request.POST.get('automobile_id')
        return executeAutomobileUpdate(request, automobile_id, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        """Browsers don't seem to support PUT..."""
        self.post(self, request, *args, **kwargs)'''

# https://iheanyi.com/journal/2020/04/04/dynamic-page-titles-in-django/