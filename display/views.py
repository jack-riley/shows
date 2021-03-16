from django.shortcuts import render, redirect
from .models import Show, Network

# Create your views here.

def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {"show_list": Show.objects.all()}
    return render(request,  'all.html', context )

def new_show(request):
    return render(request, 'add.html')

def process_new_show(request):
    if request.method == "POST":
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
    return redirect('/shows')

def edit (request, val):
    pass
    context = {"current_show": Show.objects.get(id = val)}
    
    return render(request,  'edit.html', context )

def show(request, val):
    if request.method == "GET": 
        context = {"this_show": Show.objects.get(id = val)}
    
        return render(request,  'show.html', context )
    elif request.method == "POST":
        title = request.POST["title"]
        network = request.POST["network"]
        release = request.POST["release_date"]
        desc = request.POST["desc"]
        check_network = Network.objects.filter(name = network)

        if check_network:
            old_network = Network.objects.get(name = network)
            c_show = Show.objects.get(id = val)
            c_show.title = title
            c_show.network = old_network
            c_show.release_date = release
            c_show.desc = desc
            c_show.save()
        
        else:
            Network.objects.create(name = network)
            new_network = Network.objects.get(name = network)
            c_show = Show.objects.get(id = val)
            c_show.title = title
            c_show.network = new_network
            c_show.release_date = release
            c_show.desc = desc
            c_show.save()
        context = {"this_show": Show.objects.get(id = val)}
    
        return render(request,  'show.html', context)    

def delete(request, val):
    pass
    d_show = Show.objects.get(id = val)
    d_show.delete()
    
    return redirect('/shows')



