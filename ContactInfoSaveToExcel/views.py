from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
import os
import json
from CryptICE import IceKey


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
    sendMail(info["uuid"],email)

    return render(request,"send.html",{"message": f"Başvuru linki {email} adresine gönderildi"})



def sendMail(link,email):

    send_mail(
        'Başvuru Linki',
        f'Link: http://127.0.0.1:8000/form{link}',
        "mntsodev@outlook.com",
        [email]
)

def expiredLinks():
    for i in os.listdir("Jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = readJsonFile(i.strip(i[-5:]))
            startingTime=os.stat(f"Jsons/{i}").st_ctime

            generateDate=datetime.datetime.fromtimestamp(startingTime)
            now=datetime.datetime.now()
            validityTime=info["validityTime"]
            validityTime=datetime.timedelta(hours=validityTime)

            if (generateDate+validityTime) < now:
                os.remove(f"Jsons/{i}")



def generateCryptICE(email):

    data = bytes(f"{email}", encoding="UTF-8")
    key = bytearray([0x25, 0x6C, 0xC7, 0x0A, 0x00, 0x30, 0x00, 0x5C])

    ice = IceKey(1, key)

    encrypted_data = ice.Encrypt(data, True)
    return str(encrypted_data)



def readJsonFile(email):
    with open(f"Jsons/{email}.json","r") as file:
        info = json.load(file)
    return info

def writeJsonFile(email,jsonString):
    with open(f"Jsons/{email}.json","w") as file:
        json.dump(jsonString,file)



def appeal(request,uuid):
    expiredLinks()
    for i in os.listdir("Jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = readJsonFile(i.strip(i[-5:]))
            if uuid == info["uuid"]:
                personalForm = PersonalInfoForm(request.POST or None)
                education = EducationInfoForm
                foreign = ForeignLanguageInfoForm
                certificate = CertificateInfoForm
                work = WorkExperienceInfoForm
                file=FileUpload(request.FILES or None)
                reference=ReferenceInfoForm
                course=CourseInfoForm
                context = {
                    "info": info,
                    "personalForm": personalForm,
                    "education": education,
                    "foreign": foreign,
                    "certificate": certificate,
                    "works": work,
                    "file":file,
                    "reference":reference,
                    "course":course
                }




                return render(request, "appealForm.html", context)
    else:
        return HttpResponse("<h1 style='color:red; text-align:center; margin-top:2em'>Bulunamadı. Muhtemelen Linkinizin süresi dolmuş olabilir. <a href='/generate'>Formu</a> Yeniden Doldurabilirsiniz</h1>")

def copyFile(name):

    shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"AppealFormExcels/{name}.xlsx")
    if os.path.exists("AppealFormExcels/{name}.xlsx"):
        os.remove("AppealFormExcels/{name}.xlsx")
        shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"AppealFormExcels/{name}.xlsx")



def save(request):
    name = request.POST.get("firstName")
    lastName = request.POST.get("lastName")
    email = request.POST.get("email")
    copyFile(name)



def save(request):
    return HttpResponse("<h1 style='color: #0275d8;text-align: center; margin-top:3em;'>Başvurunuz Başarıyla Alınmıştır.</h1>")



