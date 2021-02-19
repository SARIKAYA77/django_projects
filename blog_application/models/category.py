from django.db import models


class CategoryModels(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        


