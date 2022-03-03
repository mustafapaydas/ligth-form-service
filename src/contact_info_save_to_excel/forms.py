from django import forms

from django.forms.widgets import NumberInput


class PersonalInfoForm(forms.Form):
    content = "form-control  pl-5"
    firstName = forms.CharField(label="Adınız",required=False,widget=forms.TextInput(attrs={"placeholder":"Adınız","class":content}))
    lastName = forms.CharField(label='Soyadınız',required=False,widget=forms.TextInput(attrs={"placeholder":"Soyadınız","class":content}))
    email = forms.EmailField(label="Doğum Yeri",required=False,widget=forms.TextInput(attrs={"placeholder":"E-mail","class":content}))

    dateOfBirth=forms.DateField(widget=NumberInput(attrs={'type': 'date',"class":content}),label="Doğum Yılı",required=False)
    birthplace = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Doğum Yeri", "class": content}),
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



class EducationInfoForm(forms.Form):
    content="form-control  pl-5"
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



class ForeignLanguageInfoForm(forms.Form):
    content="form-control  pl-5"
    degreess = (
        ("M", "Orta"),
        ("G", 'İyi'),
        ("VG", "Çok İyi")
    )
    language= forms.CharField(max_length=100,required=False,label="Yabancı Dil",widget=forms.TextInput(attrs={"class":content}))
    degree = forms.ChoiceField(choices=degreess,required=False, widget=forms.RadioSelect(),label="Seviye")
    course = forms.CharField(max_length=100,required=False, label="Öğrendiğiniz Yer",widget=forms.TextInput(attrs={"class":content}))




class PrivateInfoForm(forms.Form):
    content="form-control  pl-5"
    drivingLicence=forms.BooleanField(label="Sürücü Belgeniz Var mı?",required=False)
    licenseClassAndNo=forms.CharField(max_length=100,label="Var ise Sınıfı ve Numarası",required=False,widget=forms.TextInput(attrs={"class":content}))
    healthProblem = forms.BooleanField(label="Sağlık Probleminiz Var mı?",required=False)
    explanationProblem = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    travelRestriction = forms.BooleanField(label="Seyahat Engeliniz Var mı?",required=False)
    explanationRestriction = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    conscription = forms.BooleanField(label="Mecburi Hizmet Borcunuz Var mı?",required=False)
    conscriptionExplanation = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    policeRecord = forms.BooleanField(label="Adli Sicil Kaydınız Var mı?",required=False)
    recordExplanation = forms.CharField(max_length=100, label="Var ise Açıklayın",required=False,widget=forms.TextInput(attrs={"class":content}))
    youSmoke = forms.BooleanField(label="Sigara İçiyor musunuz?",required=False)


class WorkExperienceInfoForm(forms.Form):
    content="form-control  pl-5"
    workPlaceName = forms.CharField(max_length=50,required=False, label="İşyeri Ünvanı",widget=forms.TextInput(attrs={"class":content}))
    duty = forms.CharField(max_length=50,required=False, label="Göreviniz",widget=forms.TextInput(attrs={"class":content}))
    price=forms.CharField(max_length=50,required=False, label="Ücretiniz",widget=forms.TextInput(attrs={"class":content}))
    reasonDeparture = forms.CharField(max_length=100,required=False, label="Ayrılış Sebebi",widget=forms.TextInput(attrs={"class":content}))
    startWorkDate=forms.DateField(widget=NumberInput(attrs={'type': 'date','class':content}),label="İşe Başlama Tarihi",required=False)
    breakUpDate=forms.DateField(widget=NumberInput(attrs={'type': 'date','class':content}),label="Ayrılma Tarihi",required=False)


class DutyAndPriceInfoForm(forms.Form):
    content="form-control  pl-5"
    oldWorkPlacePrice = forms.CharField(max_length=50, required=False, label="En Son Çalıştığınız Kurumdan Aldığınız Net Ücret:",
                                    widget=forms.TextInput(attrs={"class": content}))
    startDateOfWork = forms.CharField(max_length=50, required=False, label="Ne Zaman Çalışmaya Başlayabilirsiniz?",
                           widget=forms.TextInput(attrs={"class": content}))
    intendedSalary = forms.CharField(max_length=50, required=False, label="Talep Ettiğiniz Net Ücret:",
                            widget=forms.TextInput(attrs={"class": content}))
    residenceChange = forms.CharField(max_length=100, required=False, label="Gerektiğinde İkamet Değişikliği Yapabilir misiniz?",
                                      widget=forms.TextInput(attrs={"class": content}))

class MilitaryInfoForm(forms.Form):
    content="form-control  pl-5"
    privateSoldier=forms.CharField(max_length=100, required=False, label="Er Olarak Yaptıysanız.",
                                      widget=forms.TextInput(attrs={"class": content,"value":".................ay süreyle er olarak yaptım"}))
    reserveOfficer=forms.CharField(max_length=100, required=False, label="Yedek Subay Olarak Yaptıysanız.",
                                      widget=forms.TextInput(attrs={"class": content,"value":".................ay süreyle yedek subay olarak yaptım"}))
    exempted=forms.CharField(max_length=100, required=False, label="Muafsanız Muafiyet Durumunuz.",
                                      widget=forms.TextInput(attrs={"class": content,"value":" ..............................................nedeniyle muafım"}))
    deferment=forms.CharField(max_length=100, required=False, label="Tecilliyseniz Tecil Tarihi",
                                      widget=forms.TextInput(attrs={"class": content,"value":"..................tarihine kadar tecilliyim"}))
    militaryUnit=forms.CharField(max_length=100, required=False, label="Terhis Tarihiniz ve Terhis Olduğunuz Birlik:",
                                      widget=forms.TextInput(attrs={"class": content}))



class FileUpload(forms.Form):
    
    file=forms.FileField(required=False)

class ReferenceInfoForm(forms.Form):
    content="form-control  pl-5"
    referenceName = forms.CharField(max_length=100, label="Referansınızın Adı Soyadı",required=False,widget=forms.TextInput(attrs={"class":content}))
    instutitionOfReference = forms.CharField(max_length=100, label="Referansınızın Kurumu ve Görevi", required=False,widget=forms.TextInput(attrs={"class":content}))
    referencePhoneNumber = forms.CharField(max_length=13, label="Referansınızın Telefon Numarası", required=False,widget=forms.TextInput(attrs={"class":content}))


class CourseInfoForm(forms.Form):
    content="form-control  pl-5"
    institutionName=forms.CharField(label="Eğitim veren Kuruluşun Adı",max_length=100,widget=forms.TextInput(attrs={"class":content}),required=False)
    subjectOfCourse=forms.CharField(label="Eğitimin Konusu",max_length=100,widget=forms.TextInput(attrs={"class":content}),required=False)
    date=forms.CharField(label="Hangi Tarihler Arasında",max_length=100,widget=forms.TextInput(attrs={"class":content,"placeholder":"GG/AA/YYYY-GG/AA/YYYY"}),required=False)
    howManyHours=forms.IntegerField(label="Eğitim veren Kuruluşun Adı", required=False,widget=forms.TextInput(attrs={"class":content}))

class VerifyForm(forms.Form):
    verify = forms.BooleanField(required=True,label="Onay")
    date=forms.DateField(widget=NumberInput(attrs={'type': 'date',"class":"form-control"}),label="Tarih")