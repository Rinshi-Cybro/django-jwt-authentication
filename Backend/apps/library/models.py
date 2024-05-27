from django.db import models

# Create your models here.

class Library(models.Model):
    library_name = models.CharField(max_length=50)
    library_location = models.CharField(max_length=50)

    def __str__(self):
        return self.library_name
    

class Author(models.Model): 
    author_name = models.CharField(max_length=50) 
    phone = models.IntegerField()

    def __str__(self):
        return self.author_name
    
    
class Books(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    library_name = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.book_name)    
    





    



