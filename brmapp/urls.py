
from django.contrib import admin
from django.urls import path,include,re_path
from .views import helloView,addBookView,addBook,editBook,editBookView,deleteBookView,bookview,aboutView,developerView

urlpatterns = [
    path("",helloView),
    path("view-book/",bookview),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView),
    path("about/",aboutView),
    path("developer/",developerView),
    path("home/",helloView),
    
  
]
