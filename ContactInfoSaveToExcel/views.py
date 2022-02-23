from django.shortcuts import render,HttpResponse,redirect
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .EmailHelper import *
from .JsonFileHelper import *
from .CryptHelper import *
import uuid
from django.forms import formset_factory
from .ExcelFileHelper import *
from django.contrib import messages
from .ExpirationHelper import *

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
    for i in os.listdir("Jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = readJsonFile(i.strip(i[-5:]))
            if iceLink == info["iceLink"]:

                personalForm = PersonalInfoForm(request.POST or None)

                educationForm = EducationInfoForm(request.POST or None)


                foreignFormSet=formset_factory(ForeignLanguageInfoForm,extra=0)
                foreignForm=foreignFormSet(request.POST or None)

                military = MilitaryInfoForm(request.POST or None)

                private = PrivateInfoForm(request.POST or None)

                dutyAndPrice=DutyAndPriceInfoForm(request.POST or None)

                workFormSet=formset_factory(WorkExperienceInfoForm,extra=0)
                workForm=workFormSet(request.POST or None)

                cvFile=FileUpload(request.POST or None,request.FILES or None)

                referenceFormSet=formset_factory(ReferenceInfoForm,extra=0)
                referenceForm=referenceFormSet(request.POST or None)

                courseFormSet=formset_factory(CourseInfoForm,extra=0)
                courseForm=courseFormSet(request.POST or None)

                context = {
                    "uuid":info["uuid"],
                    "personalForm": personalForm,
                    "education": educationForm,
                    "foreign": foreignForm,
                    "private": private,
                    "works": workForm,
                    "file":cvFile,
                    "reference":referenceForm,
                    "course":courseForm,
                    "military":military,
                    "duty":dutyAndPrice,
                }



                return render(request, "appealForm.html", context)
    else:
        return HttpResponse("<h1 style='color:red; text-align:center; margin-top:2em'>Bulunamadı. Muhtemelen Linkinizin süresi dolmuş olabilir. <a href='/generate'>Formu</a> Yeniden Doldurabilirsiniz</h1>")



def save(request):


    try:
        file = request.FILES["file"]
        default_storage.save(file, ContentFile(file.read()))
        if request.method == "POST":
            email = request.POST["email"]
            copyFile(email)
            xlWrite(4, 9, email, request.POST["firstName"])
            xlWrite(4, 19, email, request.POST["lastName"])
            xlWrite(5, 9, email, request.POST["email"])
            xlWrite(5, 9, email, request.POST["yearOfBirth"])
            xlWrite(5, 19, email, request.POST["bornPlace"])
            xlWrite(7, 9, email, request.POST["address"])
            xlWrite(8, 9, email, request.POST["otherPhone"])
            xlWrite(8, 16, email, request.POST["cellPhone"])
            if request.POST["gender"] == "M":
                xlWrite(6, 11, email, "X")
            if request.POST["gender"] == "F":
                xlWrite(6, 14, email, "X")
            if request.POST["gender"] == "N":
                xlWrite(6, 18, email, "X")
            xlWrite(15, 12, email, request.POST["vocationalHighSchool"])
            xlWrite(16, 12, email, request.POST["undergraduate_faculty"])
            xlWrite(17, 12, email, request.POST["postgraduate"])
            xlWrite(18, 12, email, request.POST["doctorate"])
            xlWrite(19, 12, email, request.POST["otherEducation"])
            for i in request.POST.keys():

                if "drivingLicence" == i:
                    xlWrite(39, 9, email, 'X')
                    xlWrite(39, 13, email, request.POST["licenseClassAndNo"])
                if "healthProblem" == i:
                    xlWrite(40, 9, email, 'X')
                    xlWrite(40, 13, email, request.POST["explanationProblem"])
                if "travelRestriction" == i:
                    xlWrite(41, 9, email, 'X')
                    xlWrite(41, 13, email, request.POST["explanationRestriction"])
                if "conscription" == i:
                    xlWrite(42, 9, email, 'X')
                    xlWrite(42, 13, email, request.POST["conscriptionExplation"])
                if "policeRecord" == i:
                    xlWrite(43, 9, email, 'X')
                    xlWrite(44, 13, email, request.POST["recordExplanation"])
                if "youSmoke" == i:
                    xlWrite(44, 9, email, 'X')

                if "form-__prefix__-language" == i:

                    xlWrite(23, 2, email, request.POST[i])

                if "form-__prefix__-degree" == i:

                    if request.POST[i] == "M":
                        xlWrite(23,9, email, "X")
                    if request.POST[i] == "G":
                        xlWrite(23,13, email, "X")
                    if request.POST[i] == "VG":
                        xlWrite(23,16, email, "X")
                    xlWrite(23,18,email, request.POST['X'])

                if "form-__prefix__-course" == i:
                    xlWrite(23, 18, email, request.POST[i])

                if "form-0-language" == i:

                    xlWrite(23, 2, email, request.POST[i])

                if "form-0-degree" == i:

                    if request.POST[i] == "M":
                        xlWrite(24,9, email, "X")
                    if request.POST[i] == "G":
                        xlWrite(24,13, email, "X")
                    if request.POST[i] == "VG":
                        xlWrite(24,16, email, "X")
                    xlWrite(24,18,email, request.POST['X'])

                if "form-0-course" == i:
                    xlWrite(24, 18, email, request.POST[i])

                if "form-__prefix__-workPlaceName" == i:
                    xlWrite(27,1, email, request.POST[i])
                if "form-__prefix__-duty" in i:
                    xlWrite(27, 9, email, request.POST[i])
                if "form-__prefix__-price" in i:
                    xlWrite(27,16, email, request.POST[i])
                if "form-__prefix__-reasonDeparture" in i:
                    xlWrite(27,17, email, request.POST[i])
                if "startWorkDate" in i:
                    xlWrite(27,26, email, request.POST[i])
                if "breakUpDate" in i:
                    xlWrite(27,27, email, request.POST[i])



            xlWrite(9, 9, email, request.POST["privateSoldier"])
            xlWrite(10, 9, email, request.POST["reserveOfficer"])
            xlWrite(11, 9, email, request.POST["exempted"])
            xlWrite(12, 9, email, request.POST["deferment"])
            xlWrite(13, 9, email, request.POST["militaryUnit"])







            return HttpResponse(
                "<h1 style='color: #0275d8;text-align: center; margin-top:3em;'>Başvurunuz Başarıyla Alınmıştır.</h1>")
    except:

        messages.warning(request, "Bilgilerinizi Kontrol Ediniz!")
        return HttpResponse(
            "<h1 style='color: #0275d8;text-align: center; margin-top:3em;'>Hatalı veya Eksik Bilgi Girdiniz!</h1>")











