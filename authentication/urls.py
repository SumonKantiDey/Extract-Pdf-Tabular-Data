from django.urls import path

from . import views
urlpatterns = [
    path('registration',
         views.RegistrationView.as_view({'get': 'list', 'post': 'create'}), name='registration'),
    path('authenticate_user', views.Authenticate_user.as_view({'get': 'list', }),
         name="authenticate_user")
]
