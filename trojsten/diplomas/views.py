# -*- coding: utf-8 -*-
import zipfile
import json
from tempfile import TemporaryFile

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from trojsten.diplomas.api import DiplomaGenerator, render_png
from trojsten.diplomas.forms import DiplomaParametersForm
from trojsten.diplomas.models import DiplomaTemplate, DiplomaDataSource

from wiki.decorators import get_article
from .sources import get_class


@csrf_exempt
def source_request(request, source_class):
    user_data = get_class(source_class).handle_request(request)
    return JsonResponse(user_data, safe=False)


@login_required
def diploma_sources(request, diploma_id):
    diploma = DiplomaTemplate.objects.get(pk=diploma_id)
    file_upload_source = DiplomaDataSource.objects.get(value='FileUpload')
    sources = []
    for source in [file_upload_source] + [x for x in diploma.sources.all()]:
        src = source.source_class
        sources.append({'html': src.render(),
                        'name': source.name,
                        'url': source.value
                        })
    return render(request, 'trojsten/diplomas/sources.html', {'sources': sources})


#@cache_page(60*15)
@login_required
def diploma_preview(request, diploma_id):
    diploma = DiplomaTemplate.objects.get(pk=diploma_id)
    if diploma:
        png = render_png(diploma.svg)
        return HttpResponse(png, content_type="image/png")
    else:
        return HttpResponseNotFound()


@get_article
@login_required
def view_diplomas(request, article, *args, **kwargs):
    diploma_templates = DiplomaTemplate.objects.get_queryset().order_by('name')
    editable_fields = {}
    svgs = {}
    for d in diploma_templates:
        editable_fields[d.pk] = sorted(d.editable_fields)
        svgs[d.pk] = d.svg

    if request.method == 'POST':
        form = DiplomaParametersForm(diploma_templates, request.POST, request.FILES)
        if form.is_valid():

            participants_data = form.cleaned_data['participants_data']
            separate = not form.cleaned_data['join_pdf']
            template_pk = form.cleaned_data['template']
            svg = diploma_templates.filter(pk=template_pk).get().svg

            generator = DiplomaGenerator()
            pdfs = generator.create_diplomas(participants_data, template_svg=svg, separate=separate)

            archive_file = TemporaryFile(mode='w+b')
            with zipfile.ZipFile(archive_file, 'w', zipfile.ZIP_DEFLATED) as archive:
                for name, content in pdfs:
                    archive.writestr(name, content)
            archive_file.seek(0)

            filename = timezone.now().strftime("diplom_{}_%Y_%m_%d_%H:%M:%S.zip".format(request.user.last_name))

            response = HttpResponse()
            response['Content-type'] = 'application/zip'
            response['Content-Description'] = 'File Transfer'
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            response['Content-Transfer-Encoding'] = 'binary'

            response.write(archive_file.read())

            archive_file.close()

            return response

        else:
            for field in form:
                for error in field.errors:
                    messages.add_message(request, messages.ERROR,
                                         '%s: %s' % (field.label, error))
    else:
        form = DiplomaParametersForm(diploma_templates)

    context = {
        'form': form,
        'article': article,
        'template_fields': json.dumps(editable_fields, ensure_ascii=False).encode('utf8')
    }

    return render(
        request, 'trojsten/diplomas/test_template_v2.html', context
    )
