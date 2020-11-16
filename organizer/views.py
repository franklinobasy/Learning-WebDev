from django.shortcuts import render
from django.template import Context, loader
from django.http.response import HttpResponse

from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list' : tag_list})
    html_output = template.render(context)
    return HttpResponse(html_output)

# Create your views here.
