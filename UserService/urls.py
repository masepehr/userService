from django.urls import path
from .views import *




urlpatterns = [

    path('', home,name='home'),
    path('signup/', signup,name='signup'),
    path('profile/', profileView.as_view(),name='profile'),
    path('changepassword/', changepassword,name='changepassword'),
    path('login/',login,name='login'),
    path('address/',AddressView.as_view(),name='address'),
    path('address/<int:id>/',AddressEditView.as_view(),name='addressedit')

]
