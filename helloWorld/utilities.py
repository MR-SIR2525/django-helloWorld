from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404


class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})

class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''

    def get(self, request, id):
        obj = get_object_or_404(
            self.model, id__iexact=id)
        context = {
            'form': self.form_class(instance=obj),
            self.model.__name__.lower(): obj,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, id):
        obj = get_object_or_404(
            self.model, id__iexact=id)
        bound_form = self.form_class(
            request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj,
            }
            return render(
                request,
                self.template_name,
                context)

class ObjectDeleteMixin:
    """Delete by id"""
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, id):
        obj = get_object_or_404(self.model, id__iexact=id)
        context = {self.model.__name__.lower(): obj}
        
        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = get_object_or_404(self.model, id__iexact=id)
        obj.delete()
        return HttpResponseRedirect(self.success_url)
