from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=50)
  home = models.OneToOneField('Folder', on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

class File(models.Model):
  name = models.CharField(max_length=100)
  size = models.IntegerField()
  link = models.CharField(max_length=50)
  extension = models.CharField(max_length=10)
  parent = models.ForeignKey('Folder', on_delete=models.CASCADE, related_name="files")
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

class Folder(models.Model):
  name = models.CharField(max_length=100)
  folders = models.ManyToManyField('self', related_name="parents")
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  # folders = models.ManyToManyField('self', related_name="folders")

  def __str__(self):
    return self.name