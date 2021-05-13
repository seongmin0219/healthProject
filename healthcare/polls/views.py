from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse

import datetime

def index(request):
    return HttpResponse("Hello , real world. You're at the polls index")



def renew_book_librarian(request,  pk):

    book_instance = get_object_or_404(BookInstance, pk=pk)



# Create your views here.
