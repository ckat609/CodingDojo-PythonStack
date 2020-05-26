from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('add/<int:prod_id>', views.add),
    path('remove/<int:prod_id>', views.remove),
]
