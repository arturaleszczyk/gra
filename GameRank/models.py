from django.db.models import DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField, Model, \
    TextField, CASCADE, OneToOneField
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from GameRank.admin import WebAppAdmin


# Create your models here.
# class Genre(Model):
#     # username = WebAppAdmin('username')
#     # username = ForeignKey(username.WebAppAdmin, on_delete=DO_NOTHING)
#     username = CharField(max_length=128)
#
#     def __str__(self):
#         return self.username


class GameRank1(Model):
    username = ForeignKey(User, on_delete=CASCADE)
    ranking = IntegerField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.username, self.ranking)

    # def __str__(self):
    #     return str(self.__dict__)



class Profile(Model):
    username = OneToOneField(User, on_delete=CASCADE)
    clicks_left = IntegerField()

    def __str__(self):
        return(self.__dict__)

class Wyniki(models.Model):
    gracz = models.TextField(blank=True, null=True)
    wynik = models.IntegerField(blank=True, null=True)
