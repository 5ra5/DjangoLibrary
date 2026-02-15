from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Book, Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'author', 'price', 'synopsis']

    def clean_year(self):
        year = self.cleaned_data['year']

        if year > date.today().year:
            raise ValidationError('The year published cannot be in the future.')
        
        if year < 1440:
            raise ValidationError('The printing press was not invented until 1440.')
        
        return year
    
    def clean_title(self):
        title = self.cleaned_data['title']

        if Book.objects.filter(title__iexact=title).exists():
            raise ValidationError("Provide a unique title.")
        
        return title
    
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_year', 'country']

    def clean_birth_year(self):
        birth_year = self.cleaned_data['birth_year']

        if birth_year > date.today().year:
            raise ValidationError('The birth year cannot be in the future.')
            
        return birth_year
    
    def clean_name(self):
        name = self.cleaned_data['name']

        if Author.objects.filter(name__iexact=name).exists():
            raise ValidationError("This author already exists in the database.")
        
        return name