from django.urls import path, include
from .views import *




urlpatterns = [

    path('',include('django.contrib.auth.urls')),
    path('', home,name='home'),
    path('signup/', signup.as_view(),name='signup'),
    path('profile/', profileView.as_view(),name='profile'),
    path('changepassword/', changepassword,name='changepassword'),
    path('address/',AddressView.as_view(),name='address'),
    path('address/<int:id>/',AddressEditView.as_view(),name='addressedit')

]
