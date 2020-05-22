from common.views import index, CreateUserProfile
from django.urls import path
from allauth.account.views import login, logout, signup

app_name = 'common'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', signup, name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]
