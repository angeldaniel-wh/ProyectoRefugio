#from django.contrib import messages
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm

from apps.mascota.models import Mascota


# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}

    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_view(request):
    if request.method == "POST":
         form = MascotaForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
            messages.success(request, 'Mascota guardada correctamente')
            return redirect('mascota:function_mascota_listar')
         else:
            messages.error(request, 'Ocurrio un error al guardar el formulario')
    else:
        form = MascotaForm()
    return render(request, "mascota/mascota_form.html", {'form': form})


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == "GET":
        form = MascotaForm(instance=mascota)
        print(form)
    else:
        form = MascotaForm(request.POST, request.FILES ,instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascota:function_mascota_listar')
        else:
            messages.error(request, 'Ocurrio un error al guardar el formulario')
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == "POST":
        mascota.delete()
        messages.success(request, 'Mascota eliminada correctamente')
        return redirect('mascota:function_mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota:mascota_list.html'

class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:class_mascota_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Mascota registrada exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al registrar la mascota')
        return super().form_invalid(form)


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:class_mascota_listar')
    def form_valid(self, form):
        messages.success(self.request, 'MAscota actualizada exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocurrio un error al actualizar la mascota')
        return super().form_invalid(form)


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:class_mascota_listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Mascota eliminada correctamente')
        return super(MascotaDeleteView, self).delete(request, *args, **kwargs)