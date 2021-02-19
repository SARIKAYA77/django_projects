from django.contrib import admin
from blog_application.models import CategoryModels
from blog_application.models import Author
from blog_application.models import Article

# Register your models here.
admin.site.register(CategoryModels)
admin.site.register(Author)
admin.site.register(Article)