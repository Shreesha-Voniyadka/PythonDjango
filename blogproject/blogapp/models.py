from django.db import models
from django.contrib.auth import get_user_model
# import the get_user_model which is a helper function from Django that fetches the User model for the project
# Create your models here.
User = get_user_model()
class Author(models.Model):
    # ForeignKey, with the exception that it always carries a "unique" constraint with it
    # CASCADE - Refer sql CASCADE. Automatic Deletion with Foreign Keys
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()
    def __str__(self):
        return self.user.username
class Category(models.Model):
    title = models.CharField(max_length = 20)
    subtitle = models.CharField(max_length = 20)
    thumbnail = models.ImageField()
    slug = models.SlugField()
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete =models.CASCADE)
    thumbnail = models.ImageField()
    # Model that holds two ForeignKey fields pointed at the two sides of the relation.
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    
