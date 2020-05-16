from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('book/', views.add_book_form),
    path('author/', views.add_author_form),
    path('book/<int:id>', views.view_book),
    path('author/<int:id>', views.view_author),
    path('add_book_db/', views.add_book_db),
    path('add_author_db/', views.add_author_db),
    path('add_author_to_book/<int:id>', views.add_author_to_book),
    path('add_book_to_author/<int:id>', views.add_book_to_author)
]
