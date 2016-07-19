import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from .models import Theme
from .serializer import ThemeSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes


# Create your views here.

@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def themes(request):

    snippets = Theme.objects.order_by('id')
    total= Theme.objects.count()
    last_page= (total/3)+1
    paginator = Paginator(snippets, 3)
    page_no = request.query_params.get('page', None)
    try:
        data = paginator.page(page_no)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        return JsonResponse({'flag':'false'})

    serializer = ThemeSerializer(data.object_list, many=True)
    val={'data':serializer.data,'total_pages':last_page}
    if request.META['CONTENT_TYPE'] == 'text/plain':
        return Response({'val':val}, template_name='index.html')
    else:
        return JsonResponse(val)



