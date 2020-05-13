from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('/new', views.new_blog),
    path('/create', views.create_blog),
    path('/<int:number>', views.show_blog),
    path('/<int:number>/edit', views.edit_blog),
    path('/<int:number>/delete', views.destroy_blog)
]
