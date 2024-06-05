from django.urls import path
from home.views import submit_contact_form
from home import views
from home.views import *


urlpatterns = [
    path('submit_contact_form/', submit_contact_form, name='submit_contact_form'),
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    # path('user/', user_view, name='user'),
    path('profiles/', ProfileCreateView.as_view(), name='profile-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/<int:id>', views.ProfileDetailView, name='profile-detail'),
    path('current_user_profile/', current_user_profile, name='current_user_profile'),

]