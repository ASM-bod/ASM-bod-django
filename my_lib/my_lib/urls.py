"""
URL configuration for my_lib project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import books_list,book_details , author_details,CreateAuthor

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", books_list , name = 'books_list'),
    path("book/<int:pk>", book_details , name='book_details'),
    path("author/<int:pk>", author_details, name='author_details'),
    path('author/create/', CreateAuthor.as_view(), name='create_author')

]
