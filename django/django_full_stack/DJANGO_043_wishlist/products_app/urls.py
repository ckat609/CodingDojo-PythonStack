from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add', views.add),
    path('list', views.listall),
    path('add/db', views.add_db),
    path('view/<int:prod_id>', views.view),
    path('delete/<int:prod_id>', views.delete),
]
