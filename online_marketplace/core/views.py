from django.shortcuts import render

# views.py typically contains functions or classes responsible for handling HTTP requests
# and returning HTTP responses

# Information about the browser, your API address, if it's a get or post request (or similar)
# Has to be put in on all views that we use
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')