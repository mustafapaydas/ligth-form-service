from django.db import models
import uuid

class ContactInfo(models.Model):
    firstName = models.CharField(verbose_name="Ad",max_length=50)
    lastName=models.CharField(verbose_name="Soyad",max_length=50)
    email = models.CharField(verbose_name="Email",max_length=50)
    validityTime=models.IntegerField(verbose_name="Geçerlilik Süresi",null=True)
    uniqueId=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    iceLink=models.CharField(max_length=200,verbose_name="Link Eki",null=True)
    startingTime=models.CharField(verbose_name="Ad", max_length=50,blank=True)


class PersonalInfo(models.Model):
    firstName = models.CharField(verbose_name="Ad", max_length=50,blank=True)
    lastName = models.CharField(verbose_name="Soyad", max_length=50,blank=True)

    gender = (
        ('M', "Erkek"),
        ('F', 'Kadın'),
        ('N', "Belirtmek İstemiyorum")
    )

    gender = models.CharField(choices=gender,max_length=2,blank=True)
    address=models.TextField(max_length=200,verbose_name="Adres",blank=True)
    cellPhone=models.CharField(max_length=13,verbose_name="Cep Telefon Numaranız",blank=True)
    homePhone=models.CharField(max_length=13,verbose_name="Ev Telefonu Numaranız",blank=True)
class EducationInfo(models.Model):
    vocationalHighSchool=models.CharField(max_length=100,blank=True,verbose_name="Meslek Yüksek Okulu")
    undergraduate_faculty = models.CharField(max_length=200,blank=True,verbose_name="Lisans(Fakülte)")
    postgraduate = models.CharField(max_length=100,blank=True,verbose_name="Yüksek Lisans")
    doctorate = models.CharField(max_length=100,blank=True,verbose_name="Doktora")
    otherEducation= models.CharField(max_length=100,blank=True,verbose_name="Varsa Devam Eden Diğer Eğitiminiz")

class ForeignLanguage(models.Model):
     language=models.CharField(max_length=50)
     degrees = (
         ('M', "Orta"),
         ('G', 'İyi'),
         ('VG', "Çok İyi")

     )
     degree = models.CharField(choices=degrees, max_length=2, blank=True)
     course=models.CharField(max_length=100,verbose_name="Yabancı Dil")


class CertificateInfo(models.Model):
    drivingLicence=models.BooleanField(verbose_name="Sürücü Belgeniz Var mı?")
    licenseClassAndNo=models.CharField(max_length=100,verbose_name="Var ise Sınıfı ve Numarası",blank=True)
    healthProblem = models.BooleanField(verbose_name="Sağlık Probleminiz Var mı?")
    explanationProblem = models.CharField(max_length=100, verbose_name="Var ise Açıklayın",blank=True)
    travelRestriction = models.BooleanField(verbose_name="Seyahat Engeliniz Var mı?")
    explanationRestriction = models.CharField(max_length=100, verbose_name="Var ise Açıklayın",blank=True)
    conscription = models.BooleanField(verbose_name="Mecburi Hizmet Borcunuz Var mı?")
    conscriptionExplation = models.CharField(max_length=100, verbose_name="Var ise Açıklayın",blank=True)
    policeRecord = models.BooleanField(verbose_name="Adli Sicil Kaydınız Var mı?")
    recordExplanation = models.CharField(max_length=100, verbose_name="Var ise Açıklayın",blank=True)
    youSmoke = models.BooleanField(verbose_name="Sigara İçiyor musunuz?")

class WorkExperience(models.Model):
    workPlaceName = models.CharField(max_length=50,blank=True)
    duty = models.CharField(max_length=50,blank=True)
    price=models.CharField(max_length=50,blank=True)
    reasonDeparture = models.CharField(max_length=100,blank=True)
    startWorkDate=models.DateField()
    breakUpDate=models.DateField()

class Reference(models.Model):
    referenceName = models.CharField(max_length=100, verbose_name="Referansınızın Adı Soyadı",blank=True)
    instutitionOfReference = models.CharField(max_length=100, verbose_name="Referansınızın Kurumu ve Görevi", blank=True)
    referencePhoneNumber = models.CharField(max_length=13, verbose_name="Referansınızın Telefon Numarası", blank=True)

class Course(models.Model):
    institutionName=models.CharField(verbose_name="Eğitim veren Kuruluşun Adı",max_length=100)
    subjectOfCourse=models.CharField(verbose_name="Eğitimin Konusu",max_length=100)
    date=models.CharField(verbose_name="Hangi Tarihler Arasında",max_length=100)
    howManyHours=models.IntegerField(verbose_name="Eğitim veren Kuruluşun Adı")

class File(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField()


