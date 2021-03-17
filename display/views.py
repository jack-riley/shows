from django.core.checks import messages
from django.db.models.expressions import F
from django.shortcuts import render, redirect
from .models import Show, Network
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {"show_list": Show.objects.all()}
    return render(request,  'all.html', context )

def new_show(request):
    return render(request, 'add.html')

def process_new_show(request):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST["title"]
        network = request.POST["network"]
        release = request.POST["release_date"]
        desc = request.POST["desc"]
        check_network = Network.objects.filter(name = network)

        if check_network:
            old_network = Network.objects.get(name = network)
            Show.objects.create(title = title, network = old_network, release_date = release, desc = desc)
        
        else:
            Network.objects.create(name = network)
            new_network = Network.objects.get(name = network)
            Show.objects.create(title = title, network = new_network, release_date = release, desc = desc)
        messages.success(request, "Show Sucessfully Created")
    return redirect('/shows')

def edit (request, val):
    pass
    context = {"current_show": Show.objects.get(id = val)}
    
    return render(request,  'edit.html', context )

def show(request, val):
    context = {"this_show": Show.objects.get(id = val)}
    
    return render(request, 'show.html', context)
    
def process_edit(request, val):
    pass
    errors = Show.objects.validator(request.POST)

    if len(errors,) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/edit/{val}")

    else: 
        title = request.POST["title"]
        network = request.POST["network"]
        release = request.POST["release_date"]
        desc = request.POST["desc"]
        check_network = Network.objects.filter(name = network)

        if check_network:
            edit_network = Network.objects.get(name = network)
            
        
        else:
            Network.objects.create(name = network)
            edit_network = Network.objects.get(name = network)

        c_show = Show.objects.get(id = val)
        c_show.title = title
        c_show.network = edit_network
        c_show.release_date = release
        c_show.desc = desc
        c_show.save()
        messages.success(request, "Show Sucessfully Created")
  
    return redirect(f"/shows/{val}")
            
def delete(request, val):
    pass
    d_show = Show.objects.get(id = val)
    d_show.delete()
    
    return redirect('/shows')



