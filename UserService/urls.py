from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup),
    path('', views.home,name='home'),

]