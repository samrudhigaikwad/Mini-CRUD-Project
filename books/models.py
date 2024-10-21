from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100 ) # type: ignore
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        
        return self.name
        
        

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name        
    

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
        
    def __str__(self): 
        return self.title