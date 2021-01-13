import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404


from base import mods
import zipfile

#Nuevos import
import io
import matplotlib.pyplot as plt

from django.http import HttpResponse
from django.shortcuts import render
from random import sample

def tally_to_file(voting):

    id = voting[0]["id"]
    name = voting[0]["name"]
    desc = voting[0]["desc"]
    start_date = voting[0]["start_date"]
    end_date = voting[0]["end_date"]
    question = voting[0]["question"]["desc"]

    postproc_list = voting[0]["postproc"]

    doc_name = './system_docs/Tally_Postproc_' + str(id) + '.txt'
    zip_name = './system_docs/Tally_Postproc_' + str(id) + '.zip'

    document = 'Voting with id ' + str(id) + '\n'+'Name: ' + str(name) + '\n' + 'Description: ' + str(desc) + '\n' + 'Start Date: ' + str(
        start_date) + '\n' + 'End Date: ' + str(end_date) + '\n'+'Question: ' + str(question) + '\n' + 'Options: ' + '\n'
    
    for postproc in postproc_list:
        document = document + 'Option '+str(postproc['number'])+': '+str(postproc['option']) + ' - Votes: ' + str(postproc['votes']) + '\n'

    print(document)

    f = open(doc_name, 'w')
    try:
        f.write(document)
    finally:
        f.close()
  
    doc_zip = zipfile.ZipFile(zip_name, 'w')
    doc_zip.write(doc_name, compress_type=zipfile.ZIP_DEFLATED)
 
    doc_zip.close()

class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404
        tally_to_file(r)
       # print('PRUEBA: '+str(r[0]['id']))

        return context

    def plot(request):
    # Creamos los datos para representar en el gráfico
         x = opt.option
         y = opt.votes

    # Creamos una figura y le dibujamos el gráfico
         f = plt.figure()

    # Creamos los ejes
         axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
         axes.plot(x, y)
         axes.set_xlabel("Eje X")
         axes.set_ylabel("Eje Y")
         axes.set_title("Mi gráfico dinámico")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
         buf = io.BytesIO()
         canvas = FigureCanvasAgg(f)
         canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
         response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
         f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
        response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
