from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=100, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.PositiveIntegerField()
    categories = models.CharField(max_length=200, blank=False)
    thumbnail_url = models.URLField()

class BookRewiew(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    rating = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
        )
    review= models.TextField(MinLengthValidator(10))