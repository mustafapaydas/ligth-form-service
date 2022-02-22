from django.shortcuts import render,HttpResponse

from .EmailHelper import *
from .JsonFileHelper import *
from .CryptHelper import *
import uuid
from django.forms import formset_factory
from .ExcelFileHelper import *
from .ExpirationHelper import *

from django.core.mail import send_mail
import os
import json
from CryptICE import IceKey
import uuid

import datetime
import shutil

from .Forms import *

def index(request):
    return render(request,"index.html")

def ContactForm(request):

    context={
        "validityTimes":range(3,25,3)
    }
    return render(request,"EntryForm.html",context)

def addContact(request):

    name = request.POST.get("firstName")
    lastName = request.POST.get("lastName")
    email = request.POST.get("email")
    validityTime=str(request.POST.get("validtyTime"))
    validityTime=validityTime.strip(validityTime[-5:])
    iceLink =str(generateCryptICE(email))

    applier={
        "name":name,
        "lastName":lastName,
        "email":email,
        "validityTime":int(validityTime),
        "iceLink":iceLink,
        "uuid":str(uuid.uuid1()),
    }
    writeJsonFile(email,applier)
    info=readJsonFile(email)
    sendMail(info["iceLink"],email)


    return HttpResponse(f"<h1 style='color:red; text-align:center; margin-top:2em'>Başvuru linki {email} adresine gönderildi</h1>")

def appeal(request,iceLink):
    expiredLinks()

    if verifyJson(iceLink):

        personalForm = PersonalInfoForm(request.POST or None)

        educationForm = EducationInfoForm(request.POST or None)


        foreignFormSet=formset_factory(ForeignLanguageInfoForm,extra=0)
        foreignForm=foreignFormSet(request.POST or None)

        military = MilitaryInfoForm(request.POST or None)

        certificate = CertificateInfoForm(request.POST or None)

        dutyAndPrice=DutyAndPriceInfoForm(request.POST or None)

        workFormSet=formset_factory(WorkExperienceInfoForm,extra=0)
        workForm=workFormSet(request.POST or None)

        cvFile=FileUpload(request.POST or None,request.FILES or None)

        if cvFile.is_valid():
            cvFile.save()

        referenceFormSet=formset_factory(ReferenceInfoForm,extra=0)
        referenceForm=referenceFormSet(request.POST or None)

        courseFormSet=formset_factory(CourseInfoForm,extra=0)
        courseForm=courseFormSet(request.POST or None)

        context = {

            "personalForm": personalForm,
            "education": educationForm,
            "foreign": foreignForm,
            "certificate": certificate,
            "works": workForm,
            "file":cvFile,
            "reference":referenceForm,
            "course":courseForm,
            "military":military,
            "duty":dutyAndPrice,
        }
        names = ["firstName", "lastName", "email", "yearOfBirth", "bornPlace", "address", "cellPhone", "otherPhone"]
        if request.method == "POST":
            email = request.POST["email"]
            copyFile(email)
            for i in request.POST.keys():

                if i == names[0]:
                    xlWrite(4, 9, email, request.POST[i])
                if i == names[1]:
                    xlWrite(4, 19, email, request.POST[i])
                if i == names[2]:
                    xlWrite(5, 9, email, request.POST[i])
                if i == names[3]:
                    xlWrite(5, 9, email, request.POST[i])
                if i == "gender":
                    if request.POST[i] == "M":
                        xlWrite(6, 11, email, "X")
                    if request.POST[i] == "F":
                        xlWrite(6, 14, email, "X")
                    if request.POST[i] == "N":
                        xlWrite(6, 18, email, "X")
                if i == names[4]:
                    xlWrite(5, 19, email, request.POST[i])

            return HttpResponse(
                "<h1 style='color: #0275d8;text-align: center; margin-top:3em;'>Başvurunuz Başarıyla Alınmıştır.</h1>")


        return render(request, "appealForm.html", context)
    else:
        return HttpResponse("<h1 style='color:red; text-align:center; margin-top:2em'>Bulunamadı. Muhtemelen Linkinizin süresi dolmuş olabilir. <a href='/generate'>Formu</a> Yeniden Doldurabilirsiniz</h1>")












