from django.contrib.auth.models import User
from django.db import models




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()


class Adress(models.Model):
    ostan_choices=(
        ('teh','تهران'),
        ('shiraz','شیراز'),
        ('esfahan','اصفهان'),
        ('tabriz','تبریز')
    )
    ostan=models.CharField(max_length=255,choices=ostan_choices,null=False)
    adress_detail=models.TextField(max_length=500,null=False,blank=False)
    pelak=models.CharField(max_length=50,null=False,blank=False)
    # TODO: need length validations
    code_posti=models.CharField(max_length=100,null=False,blank=False)
    phone_number=models.CharField(max_length=11,null=False,blank=False)
    home_phone_number=models.CharField(max_length=11,null=True,blank=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)







