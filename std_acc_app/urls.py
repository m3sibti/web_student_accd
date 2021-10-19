from django.urls import path
from std_acc_app import views

'''
All important urls for routing are written here
'''

urlpatterns = [
    path('', views.home, name='home'),
    path('advertisement', views.advertisement, name='advertise'),
    path('reports', views.reports, name='reports'),
    path('registration', views.user_registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('manage_ad_ll', views.manage_ad_ll, name='manage_ad_ll'),
    path('manage_ad_mod', views.manage_ad_mod, name='manage_ad_mod'),
    path('post_ad', views.post_ad, name='post_ad'),
    path('del_ad/<str:pk>', views.del_ad, name='del_ad'),
]
