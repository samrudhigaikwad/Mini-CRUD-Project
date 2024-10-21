from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BooksViewSet, BookSearchList
from . import views

router = DefaultRouter()
router.register('authors',AuthorViewSet)
router.register('Categories',CategoryViewSet)
router.register('book',BooksViewSet)


urlpatterns = [
  
    path('api/',include(router.urls)),
    path('search/', BookSearchList.as_view(), name='book-search'),
    path('',views.list_books,name='list_books'),
    path('add_books/', views.add_books, name='add_books'),
    path('update_books/<int:id>/', views.update_books, name='update_books'),
    path('add_categorys/', views.add_categorys, name='add_categorys'),
    path('add_authors/', views.add_authors, name='add_authors'),
    path('delete_books/<int:id>/', views.delete_books, name='delete_books'),

]