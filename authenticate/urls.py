from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ="index"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('create_trip/', views.create_trip, name='create_trip'),
    path('view_trip/', views.view_trip, name='view_trip'),
    path('report/', views.report, name='report'),
]

