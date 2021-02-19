from django.db import models
from blog_application.models import CategoryModels
from django.contrib.auth.models import User

class Article(models.Model):
    # image = models.ImageField(upload_to="article photos")
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    
    # authors = models.OneToOneField(Author, on_delete=models.CASCADE)
    # authors = models.ForeignKey(User, on_delete=models.CASCADE,related_name="makaleler")
    categories = models.ManyToManyField(CategoryModels, related_name="makale")

    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()


    class Meta:
        db_table = 'Article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.headline
        