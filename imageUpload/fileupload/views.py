# encoding: utf-8
import json

from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from .models import Picture
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        thumbs = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

class BasicVersionCreateView(PictureCreateView):
    template_name_suffix = '_basic_form'


class BasicPlusVersionCreateView(PictureCreateView):
    template_name_suffix = '_basicplus_form'


class AngularVersionCreateView(PictureCreateView):
    template_name_suffix = '_angular_form'


class jQueryVersionCreateView(PictureCreateView):
    template_name_suffix = '_jquery_form'


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

def viewall(request):
    pics = Picture.objects.all()
    return render(request, "fileupload/picture_list.html", {"pics": pics})

class PictureListView(ListView):
    model = Picture

#    def thumb(self, request, *args, **kwargs):
#        self.object = self.get_object()
#        self.object.thumb()
#        response = JSONResponse(True, mimetype=response_mimetype(request))
#        response['Content-Disposition'] = 'inline; filename=files.json'
#        return response

#    def render_to_response(self, context, **response_kwargs):
#        files = [ serialize(p) for p in self.get_queryset() ]
#        data = {'files': files}
#        response = JSONResponse(data, mimetype=response_mimetype(self.request))
#        response['Content-Disposition'] = 'inline; filename=files.json'
#        return response
