from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render,redirect 
from .models import Author, Books, Category
from .serializers import AuthorSerializer, BooksSerializer, CategorySerializer
# Create your views here.


def list_books(request):
    books = Books.objects.all()
    return render(request, 'books/list_books.html', {'books': books})    
    
def add_books(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        publication_date = request.POST.get('publication_date')
        summary = request.POST.get('summary')
        author_id = request.POST.get('author')
        categories_id = request.POST.getlist('categories')
        
        author = Author.objects.get(id = author_id)
        new_book = Books(title=title,publication_date=publication_date,summary=summary,author=author)      
          
        new_book.save()
        new_book.categories.set(Category.objects.filter(id__in=categories_id))

        return redirect('list_books')
    else:
        authors = Author.objects.all()
        categories = Category.objects.all()
        return render(request,'books/add_books.html',{'authors':authors,'categories':categories})
    
    
def update_books(request, id):
    book = Books.objects.get(id=id)
    authors = Author.objects.all()
    categories = Category.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        publication_date = request.POST.get('publication_date')
        summary = request.POST.get('summary')
        author_id = request.POST.get('author')
        categories_id = request.POST.getlist('categories')   
 
        author = Author.objects.get(id = author_id)
        categories=Category.objects.filter(id_in = categories_id)
        
        book.title = title
        book.publication_date = publication_date
        book.summary = summary
        book.author = author
        book.save()
        book.categories.set(categories)
        return redirect('list_books')
    context = {
        'book': book,
        'authors': authors,
        'categories': categories,
    }
    return render(request,'books/update_books.html',context)

def delete_books(request, id):
    book = Books.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'books/delete_books.html', {'book': book})


def add_authors(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_death = request.POST.get('date_of_death')
        
        new_author = Author(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death)
        new_author.save()
        return redirect('add_books')
    return render(request, 'books/add_authors.html')


def add_categorys(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        description =request.POST.get('description')
        new_category = Category(cat_name=cat_name,description=description)
        new_category.save()
        return redirect('add_books')
    return render(request, 'books/add_categorys.html')




class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookSearchList(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [SearchFilter]
    search_fields = '['title', 'author__name', 'categories__cat_name']'
    
