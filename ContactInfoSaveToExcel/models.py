from django.db import models
import uuid

class ContactInfo(models.Model):
    firstName = models.CharField(verbose_name="Ad",max_length=50)
    lastName=models.CharField(verbose_name="Soyad",max_length=50)
    email = models.CharField(verbose_name="Email",max_length=50)
    validityTime=models.IntegerField(verbose_name="Geçerlilik Süresi",null=True)
    uniqueId=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    iceLink=models.CharField(max_length=200,verbose_name="Link Eki",null=True)