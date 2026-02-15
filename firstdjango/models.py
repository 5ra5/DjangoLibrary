from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ("fiction", "Fiction"),
    ("non-fiction", "Non-Fiction"),
    ("children", "Children/YA"),
    ("romance", "Romance"),
    ("fantasy", "Fantasy"),
    ("mystery", "Mystery/Thriller"),
    ("scifi", "Science Fiction"),
    ("historical", "Historical Fiction")
]

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(default=2000)
    country = models.CharField(max_length=50, default="country")

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="Fiction"
    )