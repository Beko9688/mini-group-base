import os
import mimetypes
from django.shortcuts import render
from .models import Files, Calendar, Facts
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.encoding import escape_uri_path

def index(request):
    random_fact = Facts.objects.order_by('?')[0]
    return render(request, 'mini_module_app/index.html', {'random_fact': random_fact})

def calendar(request):
    notes = Calendar.objects.all()
    return render(request, 'mini_module_app/calendar-page.html', {'notes': notes})

def timetable(request):
    return render(request, 'mini_module_app/timetable-page.html')

def lecture(request, subject):
    type = 'Лекция'
    criterion1 = Q(subject=subject)
    criterion2 = Q(type=type)
    files = Files.objects.filter(criterion1 & criterion2)

    return render(request, 'mini_module_app/subject-page.html', {'files': files, 'type_name': type, 'subject_name': subject})

def practice(request, subject):
    type = 'Практика'
    criterion1 = Q(subject=subject)
    criterion2 = Q(type=type)
    files = Files.objects.filter(criterion1 & criterion2)

    return render(request, 'mini_module_app/subject-page.html', {'files': files, 'type_name': type, 'subject_name': subject})

def laboratory (request, subject):
    type = 'Лабораторная'
    criterion1 = Q(subject=subject)
    criterion2 = Q(type=type)
    files = Files.objects.filter(criterion1 & criterion2)

    return render(request, 'mini_module_app/subject-page.html', {'files': files, 'type_name': type, 'subject_name': subject})


def download(request, pk):
    # file_path = os.path.join(settings.MEDIA_ROOT, path)
    file = Files.objects.get(pk=pk)
    if os.path.exists(file.path()):
        with open(file.path(), 'rb') as fh:
            mime_type, _ = mimetypes.guess_type(file.path())
            response = HttpResponse(fh.read(), content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(file.name()) + file.extension
            return response
    raise Http404