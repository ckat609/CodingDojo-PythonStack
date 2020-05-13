from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.register),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
]
