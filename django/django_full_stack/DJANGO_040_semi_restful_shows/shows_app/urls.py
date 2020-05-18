from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('show/list', views.show_list),
    path('show/add', views.show_add),
    path('show/add/create', views.show_add_db),
    path('show/edit/<int:show_num>', views.show_edit),
    path('show/edit/update', views.show_edit_db),
    path('show/view/<int:show_num>', views.show_view),
    path('show/delete/<int:show_num>', views.show_delete_db),
]
