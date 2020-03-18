from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Intro(models.Model):
    name = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    profile = models.ImageField()

    def __str__(self):
        return self.name


class Abt(models.Model):
    aboutme = models.TextField(max_length=50)
    profile = models.ImageField()
    moreaboutme = models.TextField(max_length=30)

    def __str__(self):
        return self.aboutme


class Portfolio(models.Model):
    firstport = models.ImageField()
    secondport = models.ImageField()
    thirdport = models.ImageField()
    fouthport = models.ImageField()
    fifthport = models.ImageField()
    sixport = models.ImageField()
    sevenport = models.ImageField()

    def __str__(self):
        return self.firstport


class Services(models.Model):
    Ui = models.TextField(max_length=50)
    webdev = models.TextField(max_length=50)
    webdesign = models.TextField(max_length=50)
    brand = models.TextField(max_length=50)

    def __str__(self):
        return self.Ui


class Testimonials(models.Model):
    text = models.TextField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Clients(models.Model):
    client1 = models.ImageField()
    client2 = models.ImageField()
    client3 = models.ImageField()
    client4 = models.ImageField()
    client5 = models.ImageField()
    client6 = models.ImageField()

    def __str__(self):
        return self.client1
