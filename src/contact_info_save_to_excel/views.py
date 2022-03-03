from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from ..save_to_excel_for_contact_info import settings
from .email_helper import *
from .crypt_helper import *
import uuid
from django.forms import formset_factory
from django.contrib import messages
from .expiration_links_helper import *
from django.template.loader import render_to_string
from .forms import *

def index(request):
    return render(request,"index.html")

def contact_form(request):

    context={
        "validityTimes":range(3,25,3)
    }
    return render(request,"entry_form.html",context)


def add_contact(request):

    name = request.POST.get("first_name")
    lastName = request.POST.get("last_name")
    email = request.POST.get("e-mail")
    validityTime=str(request.POST.get("validity_time"))
    validityTime=validityTime.strip(validityTime[-5:])
    iceLink =str(generate_crypt_ice(email))

    applier={
        "name":name,
        "lastName":lastName,
        "email":email,
        "validityTime":validityTime,
        "iceLink":iceLink,
        "uuid":str(uuid.uuid1()),
    }
    write_json_file(email, applier)
    info=read_json_file(email)
    send_to_mail(info["iceLink"], email)


    return HttpResponse(f"<h1 style='color:red; text-align:center; margin-top:2em'>Başvuru linki {email} adresine gönderildi</h1>")

def appeal(request,ice_link):
    expired_links()
    for i in os.listdir("jsons"):
        if (i.strip(i[:-4]) == "json"):
            info = read_json_file(i.strip(i[-5:]))
            if ice_link == info["iceLink"]:

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
                    "verify":VerifyForm(request.POST or None)
                }



                return render(request, "appeal_form.html", context)
    else:
        return HttpResponse("<h1 style='color:red; text-align:center; margin-top:2em'>Bulunamadı. Muhtemelen Linkinizin süresi dolmuş olabilir. <a href='/generate'>Formu</a> Yeniden Doldurabilirsiniz</h1>")

def save(request):
    try:
        cv = request.FILES['file']  # or self.files['image'] in your form
        path = default_storage.save(cv, ContentFile(cv.read()))
        os.path.join(settings.MEDIA_ROOT, path)
        email = request.POST["email"]
        man,woman,notWantSpecify="","",""
        language=["","","","",""]
        licence,healthProblem,travelRestriction,conscription,policeRecord,youSmoke="","","","","",""
        referenceInfo=["","",""]
        negative =["","","","","",""]
        explanations=["","","","",""]
        for i in request.POST.keys():
            if "form-0-language" == i:
                language[0] = request.POST[i]
                if request.POST["form-0-degree"] == "M":
                    language[1] = "X"
                if request.POST["form-0-degree"] == "G":
                    language[2] = "X"
                if request.POST["form-0-degree"] == "VG":
                    language[3] = "X"
                language[4]= request.POST["form-0-course"]

            if "form-0-referenceName" == i:
                referenceInfo[0] =request.POST[i]
                referenceInfo[1]=request.POST["form-0-instutitionOfReference"]
                referenceInfo[2] = request.POST["form-0-referencePhoneNumber"]
            if "gender" == "M":
                man="X"
            if "gender" == "F":
                woman="X"
            if "gender" == "N":
                notWantSpecify="X"
            if "drivingLicence" == i:
                licence ="X"
                explanations[0]=request.POST["licenseClassAndNo"]
            else:
                negative[0]="Y"
            if "healthProblem" == i:
                healthProblem ="X"
                explanations[1] = request.POST["licenseClassAndNo"]
            else:
                negative[1]="Y"
            if "travelRestriction" == i:
                travelRestriction = "X"
                explanations[2] = request.POST["licenseClassAndNo"]
            else:
                negative[2]="Y"
            if "conscription" == i:
                conscription = "X"
                explanations[4] = request.POST["licenseClassAndNo"]
            else:
                negative[3]="Y"
            if "policeRecord" == i:
                policeRecord = "X"
                explanations[4] = request.POST["licenseClassAndNo"]
            else:
                negative[4]="Y"
            if "youSmoke" == i:
                youSmoke = "X"
            else:
                negative[5]="Y"

        context = {
            "firstName":request.POST["firstName"],
            "lastName":request.POST["lastName"],
            "dateOfBirth":request.POST["dateOfBirth"],
            "birthplace":request.POST["birthplace"],
            "address":request.POST["address"],
            "cellPhone": request.POST["cellPhone"],
            "otherPhone": request.POST["otherPhone"],
            "vocationalHighSchool": request.POST["vocationalHighSchool"],
            "undergraduate_faculty": request.POST["undergraduate_faculty"],
            "postgraduate": request.POST["postgraduate"],
            "doctorate": request.POST["doctorate"],
            "otherEducation": request.POST["otherEducation"],
            "privateSoldier": request.POST["privateSoldier"],
            "reserveOfficer": request.POST["reserveOfficer"],
            "exempted": request.POST["exempted"],
            "deferment": request.POST["deferment"],
            "militaryUnit": request.POST["militaryUnit"],
            "oldWorkPlacePrice": request.POST["oldWorkPlacePrice"],
            "startDateOfWork": request.POST["startDateOfWork"],
            "intendedSalary": request.POST["intendedSalary"],
            "residenceChange": request.POST["residenceChange"],
            "language":request.POST["form-__prefix__-language"],
            "course":request.POST["form-__prefix__-course"],
            "secondLanguage":language[0],
            "secondCourse":language[4],
            "referenceName":request.POST["form-__prefix__-referenceName"],
            "instutitionOfReference":request.POST["form-__prefix__-instutitionOfReference"],
            "referencePhoneNumber":request.POST["form-__prefix__-referencePhoneNumber"],
            "secondReference":referenceInfo[0],
            "secondInstutitionOfReference":referenceInfo[1],
            "secondReferencePhoneNumber":referenceInfo[2],
            "man":man,"woman":woman,"notWant":notWantSpecify,
            "licence":licence,"licenseClassAndNo":explanations[0],
            "healthProblem":healthProblem,"problem":explanations[1],
            "travelRestriction":travelRestriction,"restriction":explanations[2],
            "conscriptionExplanation":explanations[3],"conscription":conscription,
            "policeRecord":policeRecord,"recordExplanation":explanations[4],
            "youSmoke":youSmoke, "negatives" :negative,

        }

        transferInfo = render_to_string("appealForm.xml",context)
        with open(f"appeal_form_excels/{email}.xls","w",encoding="utf-8") as xls:
            xls.write(transferInfo)
        send_to_file(email,f"appeal_form_excels/{email}.xls")

        return HttpResponse("<h2>Başvurunuz Başarıyla Alınmıştır. Sağlıklı Günler Dileriz.</h1>")
    except:
        messages.warning(request, "Bilgilerinizi Kontrol Ediniz!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))