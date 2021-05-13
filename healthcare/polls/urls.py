from django.urls import path

from . import views
from . import forms

urlpatterns = [

    # name 인수는 template 을 가리킨다
    path('', views.index, name= 'index'),
]

urlpatterns += [

    path('', forms.healthCareForm, name='renew-book-librarian')

]
