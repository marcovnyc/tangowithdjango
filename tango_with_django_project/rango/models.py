from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    view = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self): # For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=300)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self): # For Python 2, use __str__ on Python 3
        return self.title
  
