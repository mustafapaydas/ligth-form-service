from django.urls import path

from .views import contact_form, add_contact, appeal, index, save

urlpatterns = [
    path("",index),
    path("generate", contact_form, name="generate"),
    path("send", add_contact, name="addContact"),
    path("form<str:ice_link>",appeal,name="form"),
    path("save",save,name="saveInfo")

]


