from django.urls import path
from . import views
from .views import joblist,create,Update,Delete,form
urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
     path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signout',views.signout,name='signout'),
    path('apply',joblist.as_view(), name='apply'),
    path('profile',create.as_view(),name='profile'),
    path('update/<int:pk>',Update.as_view(),name = 'update'),
    path('delete/<int:pk>',Delete.as_view(),name = 'delete'),
    path('form/<int:pk>',form.as_view(),name = 'form'),
]