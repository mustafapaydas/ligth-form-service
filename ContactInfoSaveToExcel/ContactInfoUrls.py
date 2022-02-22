from django.urls import path

from .views import  ContactForm,addContact,appeal,index,save

urlpatterns = [
    path("",index),
    path("generate",ContactForm,name="generate"),
    path("send",addContact,name="addContact"),
    path("form<str:iceLink>",appeal,name="form"),
    path("save",save,name="saveInfo")

]


