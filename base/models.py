from django.db import models
from django.utils import timezone
# Create your models here.


class blog(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    description     = models.CharField(max_length = 200,default = "Author not provied any description")
    content         = models.CharField(max_length = 2000,default = "Author not provied any description")
    blog_profile_img = models.CharField(max_length = 2000,default = "https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X")
    categories = models.CharField(max_length = 200)
    updated_date    = models.DateField(default=timezone.now())


class orders(models.Model):
    id              = models.IntegerField(primary_key=True)
    Full_Name           = models.CharField(max_length = 200,default='UnTitled')
    Food_Name           = models.CharField(max_length = 200,default='UnTitled')
    Number           = models.IntegerField()
    Food_Details           = models.CharField(max_length = 200,default='UnTitled')
    Your_Address           = models.CharField(max_length = 200,default='UnTitled')
    How_Much           = models.CharField(max_length = 200,default='UnTitled')
    