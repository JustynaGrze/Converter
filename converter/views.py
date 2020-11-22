from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Converter


# Create your views here.
def index(request):
    all_converters = Converter.objects.all()
    # html =''
    # for con in all_converters:
    #     url = f'/converter/{con.id}'
    #     html += f'<a href="{url}">{con.name}</a><br>'
    context = {
        'masthead_title': "Let's convert some files!",
        'masthead_subtitle': "Manual work is for chums, right? Let's do some converting and have a sandwich!",
        'all_converters': all_converters,
    }
    return render(request, 'converter/index.html', context)


def converter(request, converter_id):
    con = Converter.objects.get(id=converter_id)
    context = {
        'masthead_title': con.name,
        'masthead_subtitle': con.description,
        'con': con,
    }
    return render(request, 'converter/converter.html', context)


def convert(request, converter_id):
    return HttpResponse(f"<h1>Converter {converter_id} converted!!</h1>")
