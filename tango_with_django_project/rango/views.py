from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = { 'boldmessage': " The matrix is a system Neo, that system is our enemy"}    

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives eaiser.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("The Matrix is a fake reality, do you want to take the blue or redpill? <br/><a href='/rango/'>Go back to the portal!</a>")
