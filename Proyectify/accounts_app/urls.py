from django.urls import path
from . import views
from .views import logout_user



urlpatterns = [
    path('login/', views.login_layout, name="login"),
    path('loged/', views.loged, name="loged"),
    path('logout/', logout_user, name='logout_user'),
]
