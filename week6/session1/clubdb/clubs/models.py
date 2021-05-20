from django.db import models
# Create your models here.
from django.db import models
from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        # email validation
        # Email Pattern
        # Email should be unique
       
        # password validation -
        # password should be atleast 8 characters long
        # password should match confirm password
        
        return errors

    def register(self, postData):
        # bcrypt - Encrypt password 
        # create user
        # Return user
        pass
        
    def authenticate(self, email, password):
        # Find user in database
        # bcrypt
        pass

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClubManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Club name must have at least 2 characters."        
        if len(postData['desc'])< 2:
            errors["desc"] =  "Club name must have at least 5 characters."
        # date validations - 
        # date should not be empty 
        # start date should be less then end date
       
        return errors
    def most_popular_club(self):
        return "most_popular_club.name"

class Club(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    owner = models.ForeignKey(User, related_name = "clubs",on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name = "joined_clubs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            
    objects= ClubManager()