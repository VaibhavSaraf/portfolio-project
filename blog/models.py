from django.db import models

# Create your models here.
    
class Blog(models.Model):
    title = models.CharField(max_length=255)

    pub_date = models.DateTimeField()

    body = models.TextField()

    image = models.ImageField(upload_to='images/')


# Create A Blog model

# Add the blog app to the setting

# Create migration

# migrate

# add to admin