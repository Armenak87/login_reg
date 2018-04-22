from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First Name must be 2 characters minimum")
        if (postData['first_name']).isalpha() == False:
            errors.append("First Name can only contain letters")
        if len(postData['last_name']) < 2:
            errors.append("Last Name must be 2 characters minimum")
        if (postData['last_name']).isalpha() == False:
            errors.append("Last Name can only contain letters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email Address")
            #The line below check for duplicate emails
        if (User.objects.filter(email = postData['email']).count()) > 0:
            errors.append("Email already exists")
        # if User.objects.filter(email=['email']).exists():
            # errors.append("Email already exits")
            errors.append("Password and confirmation don't match")        
        if len(postData['password']) < 8:
            errors.append("Password must be 8 chracters minimum")
        if postData['password'] != postData['confirm_password']:
            errors.append("Password and confirmation don't match")
        return errors

    def create_user(self, clean_data):
        
        hashed_pw = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name = clean_data['first_name'],
            last_name = clean_data['last_name'],
            email = clean_data['email'],
            password = hashed_pw
        )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "First Name: {}, Last Name: {}, Email: {}".format(self.first_name, self.last_name, self.email)