from django.shortcuts import render
from django.http import JsonResponse
from .models import Estado, Municipio
from .forms import MunicipioForm

def municipio_view(request):
    estados = Estado.objects.all()
    form = MunicipioForm()
    return render(request, 'ubicaciones/municipio_form.html', {'form': form, 'estados': estados})

def get_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre')
    return JsonResponse(list(municipios), safe=False)
