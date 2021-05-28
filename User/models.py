from django.db import models

# User Model
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

# Post Model
class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

    def __str__(self):
        return self.text

