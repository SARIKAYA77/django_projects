from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    # article = models.ManyToManyField(Article, related_name="yazar" )
    #bir makalenin birden cok yazara atanabilmesi
    class Meta:
        db_table = 'Author'

    def __str__(self):
        return self.name