from django.db import models

class Users(models.Model) :
    #id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    empId = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    isActive = models.BooleanField()
    isOnline = models.IntegerField()

    def __str__(self) :
        return self.fullName
