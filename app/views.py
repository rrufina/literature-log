from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Poem
from .forms import PoemForm

# Create your views here.
def index(request):
    poem_list = Poem.objects.all
    template = loader.get_template('poems/index.html')
    context = {'poem_list': poem_list}
    # output = ', '.join([p.title for p in poem_list])
    return HttpResponse(template.render(context, request))

def detail(request, poem_id):
    poem = Poem.objects.get(pk=poem_id)
    template = loader.get_template('poems/text.html')
    context = {'title': poem.title, 'author': poem.author, 'text':poem.text}
    return HttpResponse(template.render(context, request))

def add(request):
    if request.method =='POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = PoemForm()
        template = 'poems/add.html'
        context = {'form': form}
        return render(request, template, context)
