from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

# views.py typically contains functions or classes responsible for handling HTTP requests
# and returning HTTP responses

# Information about the browser, your API address, if it's a get or post request (or similar)
# Has to be put in on all views that we use
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })