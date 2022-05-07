from django.db import models
from Users.models import Users

class MainUser(models.Model):
    Owner = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='Owner',related_name='mainUser_owner')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')
    identifierـcode = models.CharField(unique=True,max_length=30,verbose_name='Identifier code')
    places = models.IntegerField(default=1,verbose_name='Places')

    def __str__(self):
        return self.identifierـcode

class Rusers(models.Model):
    main = models.ForeignKey(MainUser,on_delete=models.CASCADE,verbose_name='Main')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode


class Lusers(models.Model):
    main = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Main')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode



