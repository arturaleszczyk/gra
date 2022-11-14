from django.db.models import DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField, Model, TextField, CASCADE, OneToOneField
from django.contrib.auth.models import User

# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.__dict__)


class Url(Model):
    url = CharField(max_length=256)
    short_code = CharField(max_length=8)

class Profile(Model):
   user = OneToOneField(User, on_delete=CASCADE)
   clicks_left = IntegerField()