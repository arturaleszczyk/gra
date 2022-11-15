from django.db.models import DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField, Model, TextField, CASCADE, OneToOneField
from django.contrib.auth.models import User

# Create your models here.
class Genre(Model):
    username = CharField(max_length=128)

    def __str__(self):
        return self.username


class GameRank1(Model):
    username = ForeignKey(Genre, on_delete=DO_NOTHING)
    ranking = IntegerField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.__dict__)


class Profile(Model):
   username = OneToOneField(User, on_delete=CASCADE)
   clicks_left = IntegerField()