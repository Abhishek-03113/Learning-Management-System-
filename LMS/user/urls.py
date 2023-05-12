
from django.urls import path,include
from user import views

urlpatterns = [
    path('',views.hello,name='hello'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout_user,name='logout'),

]