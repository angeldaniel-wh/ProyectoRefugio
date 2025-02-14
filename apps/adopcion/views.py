from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
#from pyexpat.errors import messages

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm


# Create your views here.
def index_adopcion(request):
    return  HttpResponse("Hello, world. soy la pagina principal de la app Adopcion")

def solicitud_list(request):
    solicitudes = Solicitud.objects.all().order_by('id')
    contexto = {'solicitudes': solicitudes}
    return render(request, 'adopcion/solicitud_list.html', contexto)

def solicitud_create(request):
    form = SolicitudForm()
    form2 = PersonaForm()
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        form2 = PersonaForm(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            messages.success(request, 'Solicitud creada correctamente')
            return HttpResponseRedirect(reverse('adopcion:function_solicitud_listar'))
        else:
            messages.error(request, f'Ocurrió un error al actualizar el formulario')
    return render(request, 'adopcion/solicitud_form.html',  {'form': form, 'form2': form2})

def solicitud_update(request, pk):
    model = Solicitud
    second_model = Persona
    form_class = SolicitudForm
    second_form_class = PersonaForm
    solicitud = model.objects.get(id=pk)
    persona = second_model.objects.get(id=solicitud.persona.id)
    form = form_class(instance=solicitud)
    form2 = second_form_class(instance=persona)

    if request.method == 'POST':
        form = form_class(request.POST, instance=solicitud)
        form2 = second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            messages.success(request, 'Formulario guardado correctamente')
            return HttpResponseRedirect(reverse('adopcion:function_solicitud_listar'))
        else:
            messages.error(request, f'Ocurrió un error al actualizar el formulario')
    return render(request, 'adopcion/solicitud_form.html', {'id': pk, 'form': form, 'form2': form2})

def solicitud_delete(request, pk):
    solicitud = Solicitud.objects.get(id=pk)
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'Solicitud eliminada correctamente')
        return HttpResponseRedirect(reverse('adopcion:function_solicitud_listar'))
    return render(request, 'adopcion/solicitud_delete.html', {'solicitud': solicitud})

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:class_solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            if 'form' not in context:
                context['form'] = self.form_class(self.request.POST)
            if 'form2' not in context:
                context['form2'] = self.second_form_class(self.request.POST)
        else:
            if 'form' not in context:
                context['form'] = self.form_class()
            if 'form2' not in context:
                context['form2'] = self.second_form_class()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            print(self.get_success_url())
            messages.success(request, 'Solicitud guardado correctamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, f'Ocurrió un error al actualizar la solicitud')
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model= Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    prueba = "test"
    success_url = reverse_lazy('adopcion:class_solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)

        print(solicitud)
        print(persona)

        print(self.prueba)
        print(self.kwargs)

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=persona)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            print(form.cleaned_data.get("numero_mascotas"))
            print(form)
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            messages.success(request, 'Solicitud actualizada con éxito')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, f'Ocurrió un error al actualizar la solicitud')
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name =  'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:class_solicitud_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Solicitud eliminada correctamente')
        return super(SolicitudDelete, self).delete(request, *args, **kwargs)