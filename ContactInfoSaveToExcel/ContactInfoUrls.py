from django.urls import path

from .views import  ContactForm,addContact,appeal,save,index

urlpatterns = [
    path("",index),
    path("generate",ContactForm,name="generate"),
    path("send",addContact,name="addContact"),
    path("form<str:uuid>",appeal,name="form"),
    path("saveInfo",save,name="contact")
]

