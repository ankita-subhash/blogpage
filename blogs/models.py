from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('Pending', 'Pending')
    )
   
    title = models.CharField(max_length= 100, blank= False, null=True )
    description = models.CharField(max_length= 160 , blank= False, null=True)
    content = RichTextField()
    slug = models.SlugField(max_length= 100, unique= True, blank= False, null=True)
    image = models.ImageField(null= True, blank= True, upload_to= 'images/')
    status = models.CharField(max_length= 15, choices= STATUS, blank= False, null=True)
    Date = models.DateField(auto_now= True)

    def __str__(self):
        return self.title

