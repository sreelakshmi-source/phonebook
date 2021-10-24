from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from .forms import updateForms

# Create your views here.
def home(request):
   list = phonebook.objects.all()
   if request.method == "POST":
      name = request.POST.get("name")
      phonenum = request.POST.get("phonenum")
      add= request.POST.get("address")
      email = request.POST.get("email")
      obj = phonebook(name=name,phonenum=phonenum,address=add,email=email)
      obj.save()
   return  render (request,"home.html",{"list":list})

def delete (request,id):
   item = phonebook.objects.get(id=id)
   if request.method == "POST":
      item.delete()
      return redirect("/")
   return render (request,"delete.html")


def update(request, id):
   num = phonebook.objects.get(id=id)
   form = updateForms(request.POST or None, instance=num)
   if form.is_valid():
      form.save()
      return redirect('/')
   return render(request, 'update.html', {"item": num, "form": form})

def search(request):
      num = None
      query = None
      if 'q' in request.GET:
         query = request.GET.get('q')  # gets q in request to query
         num = phonebook.objects.all().filter(Q(name__contains=query))

      return render(request, 'search.html', {'num': num})


