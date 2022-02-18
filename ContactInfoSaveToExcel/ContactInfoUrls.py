from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  ContactForm,addContact,appeal,save,index

urlpatterns = [
    path("",index),
    path("generate",ContactForm,name="generate"),
    path("send",addContact,name="addContact"),
    path("form<str:uuid>",appeal,name="form"),
    path("saveInfo",save,name="saveInfo"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
