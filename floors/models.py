from django.db import models
from  django.contrib.auth.models import User,AbstractUser,PermissionsMixin

# Create your models here.

class Register_user(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #phone_munber=models.CharField(max_length=15,null=True,unique=True,blank=True)
    email=models.EmailField(null=True,unique=True)

    #
    # def __str__(self):
    #     return self.names

    class Meta:
        verbose_name='user'
        verbose_name_plural='user'




class floors(models.Model):
    room_share = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
    ]

    user=models.ForeignKey(Register_user,on_delete=models.CASCADE )
    floor_number=models.IntegerField(blank=True)
    room_number=models.IntegerField(blank=True)
    room_sharing = models.CharField(max_length=10, choices=room_share)
   # company_data=models.ForeignKey(Company_details,on_delete=models.CASCADE)
    amount_paid=models.BooleanField(default='',blank=True)
    joining_data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.floor_number} + {self.room_number}"

    class Meta:
        verbose_name = 'floors'
        verbose_name_plural = 'floors'


class person_details(models.Model):
    first_name=models.CharField(max_length=70,null=True,blank=True)
    last_name=models.CharField(max_length=140,null=True,blank=True)
    father_name=models.CharField(max_length=170,null=True,blank=True)
    phone_number=models.CharField(max_length=14,null=True,blank=True,unique=True)
    telephone_name=models.CharField(max_length=13,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)
    parement_address=models.TextField(max_length=240,null=True,blank=True)
    state=models.CharField(max_length=189,null=True,blank=True)
    country=models.CharField(max_length=184,null=True,blank=True)


    def __str__(self):
        return  f"{self.last_name}+{self.email}+{self.father_name}+{self.phone_number}"

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'person_details'



class Company_details(models.Model):

    company_name=models.CharField(max_length=149,null=True,blank=True)
    working_timing=models.TimeField()
    address=models.TextField(max_length=250,null=True)

    def __str__(self):
        return f"{self.company_name}+{self.address}"
    class Meta:
        verbose_name='company'
        verbose_name_plural='company_details'







