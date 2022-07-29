import re
from django.shortcuts import render, redirect
from .models import Link
from .forms import AddLinlForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinlForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups ...deberia entrar el nombre o el precio"
        except:
            error = "Ups... algo salio mal"

    form = AddLinlForm()

    qs = Link.objects.all()
    items_no = qs.count()
    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)
    context = {
        'qs':qs,
        'items_no':items_no,
        'no_discounted':no_discounted,
        'form':form,
        'error':error
    }
    return render(request, 'links/main.html', context)

class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/confirm_delete.html'
    success_url = reverse_lazy('home')

def update_price(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')