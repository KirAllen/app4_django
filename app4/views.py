import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, Product

logger = logging.getLogger(__name__)

def product(request):
    if request.method == 'POST':
        form = Product(request.post, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Got {name=}, {price=}, {amount=}.')
    else:
        form =Product()
    return render(request, 'app4/product.html', {'form': form})



def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Got {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'app4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Got {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'app4/many_fields_form.html', {'form': form})
