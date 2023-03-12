from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    views ={}
    views['detail'] = Detail.objects.all()
    return render(request, 'index.html', views)


def create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        address = request.POST['address']
        data = Detail.objects.create(
            firstname = firstname,
            address = address,
        )
        data.save()
    return redirect('home')

    # details = Detail(firstname=request.POST['firstname'], address=request.POST['address'])
    # details.save()
    # return redirect('home')



def edit(request, id):
    views= {}
    views['edits'] = Detail.objects.get(id=id)
    return render(request, 'edit.html', views)


def update(request, id):
    details = Detail.objects.get(id=id)
    details.firstname = request.POST['firstname']
    details.address = request.POST['address']
    details.save()
    return redirect('home')

    # data = Detail.objects.get(id=id)
    # data.save()
    # if request.method == 'POST':
    #     firstname = request.POST['firstname']
    #     address = request.POST['address']
    #     data = Detail.objects.create(
    #         firstname = firstname,
    #         address = address,
    #     )
    #     data.save()
    # return redirect('home')


def delete(request,id):
    remove = Detail.objects.get(id=id)
    remove.delete()
    return redirect('home')

