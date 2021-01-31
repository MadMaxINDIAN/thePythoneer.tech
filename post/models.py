from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    content = models.TextField()
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    github = models.CharField(max_length=60, null=True, blank=True)
    linkedin = models.CharField(max_length=60, null=True, blank=True)
    personal_website = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPostComment(models.Model):
    comment = models.TextField()

    def __str__(self):
        return self.comment

class BlogPost(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    team = models.ManyToManyField(Author)
    whatsapp_message = models.CharField(max_length=1000,null=True)
    facebook_link = models.CharField(max_length=100,null=True)
    comments = models.ManyToManyField(BlogPostComment,blank=True)
    # TODO : ADD COMMENTS
    # TODO : ADD FEEDBACK
    feedback_upvote = models.IntegerField(default=0)
    feedback_loved = models.IntegerField(default=0)
    feedback_amazed = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class EmailIPLocator(models.Model):
    email = models.EmailField()
    city = models.TextField
    country = models.TextField
    asname = models.TextField
    isp = models.TextField
    lat = models.FloatField()
    lon = models.FloatField()
    ip = models.IPAddressField
    zip_code = models.IntegerField()
    
    def __str__(self):
        return self.email
