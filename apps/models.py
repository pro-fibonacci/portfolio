from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Intro(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    profile1 = models.ImageField()

    def __str__(self):
        return self.name


class Abt(models.Model):
    aboutme = models.TextField(max_length=5000)
    profile = models.ImageField()
    moreaboutme = models.TextField(max_length=3000)

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

    def __img__(self):
        return self.firstport


class Services(models.Model):
    Ui = models.TextField(max_length=5000)
    webdev = models.TextField(max_length=5000)
    webdesign = models.TextField(max_length=5000)
    brand = models.TextField(max_length=5000)

    def __str__(self):
        return self.Ui


class Testimonials(models.Model):
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Clients(models.Model):
    client1 = models.ImageField()
    client2 = models.ImageField()
    client3 = models.ImageField()
    client4 = models.ImageField()
    client5 = models.ImageField()
    client6 = models.ImageField()

    def __img__(self):
        return self.client1
