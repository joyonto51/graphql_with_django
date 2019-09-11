from django.db import models

# Create your models here.
class Writer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Edition(models.Model):
    edition = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

    def __str__(self):
        return "{} - {}".format(self.edition, self.year)


class Book(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publication = models.CharField(max_length=30)
    editions = models.ManyToManyField(Edition)

    def __str__(self):
        return self.title