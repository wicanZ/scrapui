from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator 
from django.core.exceptions import ValidationError
import re
# Create your models here.



class ScrapItem(models.Model ) :
    regex = RegexValidator(regex=r"(0|91)?[6-9][0-9]{9}",message='Invalid phone number ')
    name = models.CharField(max_length=100)
    user = models.ForeignKey( User , on_delete=models.CASCADE )
    address = models.CharField(max_length=100, blank=False)
    phone = models.CharField(validators=[regex] ,max_length=12)
    descriptive = models.TextField()
    #city = models.CharField(max_length=50)
    #state = models.CharField(max_length=50)
    zip  = models.IntegerField()
    status = models.BooleanField(default=False)
    images = models.ImageField( upload_to ="scrapui/")
    created   = models.DateTimeField( auto_now_add=True )
    updated   = models.DateTimeField( auto_now=True )


    def __str__( self ) :
        return self.name 

class MultiScrapImage( models.Model ):
    name   = models.ForeignKey( ScrapItem , default=None, on_delete=models.CASCADE )
    images = models.ImageField( upload_to = 'images/' )