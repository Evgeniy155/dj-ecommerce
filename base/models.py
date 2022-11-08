from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    name = models.CharField(max_length = 20, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null = True, blank = True)

    avatar = models.ImageField(null = True, default = "avatar.svg", blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name[:50]



class Product(models.Model):

    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(default = 'empty.png', null = True, blank = True)
    availiable = models.BooleanField(default = True)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    discount = models.FloatField(null = True)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Comment(models.Model):

    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body


