from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.views.generic import View

from .forms import *
from django.shortcuts import render, redirect

from .models import Adress


def home(request):
    return render(request,'index.html')
# def signup(request):
#     if request.method=='POST':
#         # form=UserCreationForm(request.POST)
#         form=signUpForm(request.POST)
#
#         if form.is_valid() :
#             user=form.save()
#             user.refresh_from_db()
#             user.profile.birthdate=form.cleaned_data['birthdate']
#             user.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request=request,user=user)
#             return redirect('profile')
#
#
#     else:
#         form=signUpForm()
#     return render(request,'UserService/signup.html',{'form':form})
class signup(View):
    def post(self,request):
        form = signUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthdate = form.cleaned_data['birthdate']
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            return redirect('profile')
    def get(self,request):
        form = signUpForm()
        return render(request, 'UserService/signup.html', {'form': form})



class profileView(LoginRequiredMixin,View):

    def get(self,request):
        user=request.user
        adresses=Adress.objects.all().filter(user=user)
        return render(request,'UserService/profile.html',{'adresses':adresses})

    def put(self,request):
        pass

    def post(self,request):

        for postItem in request.POST:

            if postItem=='addr_add' :
                return redirect('address')

            # elif  postItem.startswith('edit'):
            #     addressId=postItem.replace('edit_','')
            #     return redirect('addressedit')
                
            elif postItem.startswith('delete'):
                addressId=postItem.replace('delete_','')
                Adress.objects.filter(id=int(addressId)).delete()

                return redirect('profile')
            elif 'update_profile'==postItem:


                    # TODO:
                pass

        return render(request,'UserService/profile.html')

class AddressView(LoginRequiredMixin,View):

    def get(self,request):
        ostans=dict(Adress.ostan_choices)
        return render(request,'UserService/address_view.html',context={'ostans':ostans})

        
    def post(self,request):
        ostan=request.POST['ostan_select']
        address_detail=request.POST['address_detail']
        pelak=request.POST['pelak']
        code_posti=request.POST['code_posti']
        phone_number=request.POST['phone_number']
        if 'home_phone_number'  in  request.POST:
            home_phone_number= request.POST['home_phone_number']

            newaddr=Adress(ostan=ostan,adress_detail=address_detail,
                           pelak=pelak,
                           code_posti=code_posti,
                           phone_number=phone_number,
                           home_phone_number=home_phone_number,
                           user=request.user)
        else:
            newaddr=Adress(ostan=ostan,adress_detail=address_detail,
                           pelak=pelak,
                           code_posti=code_posti,
                           phone_number=phone_number,
                           user=request.user)
        newaddr.save()
        return redirect('profile') 


class AddressEditView(LoginRequiredMixin,View):

    def get(self,request,id):
        # address=Adress.objects.get(id=7)
        ostans = dict(Adress.ostan_choices)
        address=Adress.objects.get(id=id)
        return render(request,'UserService/address_update_view.html',
                      context={'address':address,'ostans':ostans})

    def post(self,request,id):
        address = Adress.objects.get(id=id)
        address.ostan = request.POST['ostan_select']
        address.adress_detail = request.POST['address_detail']
        address.pelak = request.POST['pelak']
        address.pelak = request.POST['code_posti']
        address.phone_number = request.POST['phone_number']
        if 'home_phone_number' in request.POST:
            address.home_phone_number = request.POST['home_phone_number']

        address.save()
        return redirect('profile')



@login_required
def changepassword(request):
    if request.method=='POST':
        pass


