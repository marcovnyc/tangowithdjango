from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = { 'boldmessage': " The matrix is a system Neo, that system is our enemy"}    

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives eaiser.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')

def redpill(request):
    # Query the db for all categories as a list
    # Order the categories for the numbers of likes in descending order
    # retrieve only the top 5  or all if less than 5
    # Place the list on a context dictionary which will be passed to a template
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back
    return render(request, 'rango/redpill.html', context_dict)
