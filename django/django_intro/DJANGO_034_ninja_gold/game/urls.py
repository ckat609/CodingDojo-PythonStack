from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('process_gold', views.process_gold),
    path('process_gold/<source>', views.process_gold),
    path('reset', views.reset_all),

    # path('admin/', admin.site.urls),
]
