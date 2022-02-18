from django import forms
from .models import *
from django.forms.widgets import NumberInput
from django.forms import inlineformset_factory

class PersonalInfoForm(forms.ModelForm):
    content="form-control"
    firstName = forms.CharField(label="Adınız",required=False,widget=forms.TextInput(attrs={"placeholder":"Adınız","class":content}))
    lastName = forms.CharField(label='Soyadınız',required=False,widget=forms.TextInput(attrs={"placeholder":"Soyadınız","class":content}))
    email = forms.EmailField(label="Doğum Yeri",required=False,widget=forms.TextInput(attrs={"class" : "form-control","placeholder":"E-mail","class":content}))

    yearOfBirth=forms.DateField(widget=NumberInput(attrs={'type': 'date',"class":content}),label="Doğum Yılı",required=False)
    bornPlace = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Doğum Yeri", "class": content}),
                              required=False)
    genderChoices = (
    ("M", "Erkek"),
    ("F", 'Kadın'),
    ("N", "Belirtmek İstemiyorum")
)
    gender = forms.ChoiceField(label="Cinsiyetiniz",choices=genderChoices, widget=forms.RadioSelect(),required=False)
    address=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Adres","class":content,'rows':4}),required=False)
    cellPhone=forms.CharField(max_length=13, label="Cep Telefonu Numarası",required=False,widget=forms.TextInput(attrs={"placeholder":"Cep Telefonu","class":content}))
    otherPhone = forms.CharField(max_length=13,label="Ev Telefonu Numarası",required=False,widget=forms.TextInput(attrs={"placeholder":"Ev Telefonu","class":content}))
    file = forms.FileField()
    class Meta:
        # model = PersonalInfo
        fields=["firstName","lastName","email","yearOfBirth","bornPlace","gender","address","cellPhone","otherPhone"]

class EducationInfoForm(forms.ModelForm):
    content = "form-control"
    vocationalHighSchool = forms.CharField(max_length=100,required=False,label="Meslek Yüksek Okul",widget=forms.TextInput(attrs={
        "placeholder":"Meslek Yüksek Okul",
        "class":content
    }))
    undergraduate_faculty = forms.CharField(max_length=200,required=False,label="Lisans (Fakülte)",widget=forms.TextInput(attrs={
        "placeholder":"Lisans (Fakülte)",
        "class":content
    }))
    postgraduate = forms.CharField(max_length=100,required=False,label="Yüksek Lisans",widget=forms.TextInput(attrs={
        "placeholder":"Yüksek Lisans",
        "class":content
    }))
    doctorate = forms.CharField(max_length=100,required=False,label="Doktora",widget=forms.TextInput(attrs={
        "placeholder":"Doktora",
        "class":content
    }))
    otherEducation = forms.CharField(max_length=100,required=False,label="Varsa Devam Eden Diğer Eğitiminiz",widget=forms.TextInput(attrs={
        "placeholder":"Varsa Devam Eden Diğer Eğitiminiz",
        "class":content
    }))

    class Meta:
        model = EducationInfo
        fields = ["vocationalHighSchool", "undergraduate_faculty", "postgraduate", "doctorate", "otherEducation"]

class ForeignLanguageInfoForm(forms.ModelForm):
    content = "form-control"
    degreess = (
        ("M", "Orta"),
        ("G", 'İyi'),
        ("VG", "Çok İyi")
    )
    language= forms.CharField(max_length=100,required=False,label="Yabancı Dil",widget=forms.TextInput(attrs={"class":content}))
    degree = forms.ChoiceField(choices=degreess,required=False, widget=forms.RadioSelect(),label="Seviye")
    course = forms.CharField(max_length=100,required=False, label="Öğrendiğiniz Yer",widget=forms.TextInput(attrs={"class":content}))

    class Meta:
        model = ForeignLanguage
        fields = ["language", "degree", "course"]


class CertificateInfoForm(forms.ModelForm):
    content="form-control"
    drivingLicence=forms.BooleanField(label="Sürücü Belgeniz Var mı?",required=False)
    licenseClassAndNo=forms.CharField(max_length=100,label="Var ise Sınıfı ve Numarası",required=False,widget=forms.TextInput(attrs={"class":content}))
    healthProblem = forms.BooleanField(label="Sağlık Probleminiz Var mı?",required=False)
    explanationProblem = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    travelRestriction = forms.BooleanField(label="Seyahat Engeliniz Var mı?",required=False)
    explanationRestriction = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    conscription = forms.BooleanField(label="Mecburi Hizmet Borcunuz Var mı?",required=False)
    conscriptionExplation = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    policeRecord = forms.BooleanField(label="Adli Sicil Kaydınız Var mı?",required=False)
    recordExplanation = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    youSmoke = forms.BooleanField(label="Sigara İçiyor musunuz?",required=False)

    class Meta:
        model = CertificateInfo
        fields = ["drivingLicence", "licenseClassAndNo", "healthProblem","explanationProblem", "travelRestriction", "explanationRestriction",
                  "conscription", "conscriptionExplation", "policeRecord", "recordExplanation", "youSmoke"]
class WorkExperienceInfoForm(forms.Form):
    content="form-control"
    workPlaceName = forms.CharField(max_length=50,required=False, label="İşyeri Ünvanı",widget=forms.TextInput(attrs={"class":content}))
    duty = forms.CharField(max_length=50,required=False, label="Göreviniz",widget=forms.TextInput(attrs={"class":content}))
    price=forms.CharField(max_length=50,required=False, label="Ücretiniz",widget=forms.TextInput(attrs={"class":content}))
    reasonDeparture = forms.CharField(max_length=100,required=False, label="Ayrılış Sebebi",widget=forms.TextInput(attrs={"class":content}))
    startWorkDate=forms.DateField(widget=NumberInput(attrs={'type': 'date','class':content}),label="İşe Başlama Tarihi",required=False)
    breakUpDate=forms.DateField(widget=NumberInput(attrs={'type': 'date','class':content}),label="Ayrılma Tarihi",required=False)

    class Meta:
        model=WorkExperience
        fields=["workPlaceName","duty", "price", "reasonDeparture","startWorkDate","breakUpDate"]



class FileUpload(forms.ModelForm):

    file = forms.FileField(label="CV",required=False)
    class Meta:
        model=File
        fields=["file"]
class ReferenceInfoForm(forms.ModelForm):
    content = "form-control"
    referenceName = forms.CharField(max_length=100, label="Referansınızın Adı Soyadı",required=False,widget=forms.TextInput(attrs={"class":content}))
    instutitionOfReference = forms.CharField(max_length=100, label="Referansınızın Kurumu ve Görevi", required=False,widget=forms.TextInput(attrs={"class":content}))
    referencePhoneNumber = forms.CharField(max_length=13, label="Referansınızın Telefon Numarası", required=False,widget=forms.TextInput(attrs={"class":content}))

    class Meta:
        model = Reference
        fields=["referenceName","instutitionOfReference","referencePhoneNumber"]

class CourseInfoForm(forms.ModelForm):
    content="form-control"
    institutionName=forms.CharField(label="Eğitim veren Kuruluşun Adı",max_length=100,widget=forms.TextInput(attrs={"class":content}),required=False)
    subjectOfCourse=forms.CharField(label="Eğitimin Konusu",max_length=100,widget=forms.TextInput(attrs={"class":content}),required=False)
    date=forms.CharField(label="Hangi Tarihler Arasında",max_length=100,widget=forms.TextInput(attrs={"class":content,"placeholder":"GG/AA/YYYY-GG/AA/YYYY"}),required=False)
    howManyHours=forms.IntegerField(label="Eğitim veren Kuruluşun Adı", required=False,widget=forms.TextInput(attrs={"class":content}))

    class Meta:
        model=Course
        fields=["institutionName","subjectOfCourse","date","howManyHours"]