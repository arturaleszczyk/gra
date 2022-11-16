import re

from django.forms import (
   CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ModelForm
)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from GameRank.models import GameRank1
from datetime import date


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


# class PastMonthField(DateField):
#     def validate(self, value):
#         super().validate(value)
#         if value >= date.today():
#             raise ValidationError('Only past dates allowed here.')

    # def clean(self, value):
    #     result = super().clean(value)
    #     return date(year=result.year, month=result.month, day=1)


class GameRankForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = GameRank1
        fields = '__all__'
    username = CharField(validators=[capitalized_validator])
    ranking = IntegerField(min_value=1, max_value=100)

    # def clean_description(self):
    #     # Force each sentence of the description to be capitalized.
    #     initial = self.cleaned_data['description']
    #     sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
    #     return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].username == 'commedy' and ranking['ranking']> 1000:
            raise ValidationError(
                "Commedies aren't so good to be rated over 1000."
            )
        return result

class SingUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields =['username', 'first_name']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)

from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class SignUpForm(UserCreationForm):

   class Meta(UserCreationForm.Meta):
       fields = ['username']

   @atomic
   def save(self, commit=True):
       self.instance.is_active = False
       user = super().save(commit)
       profile = Profile(clicks_left=5, user=user)
       if commit:
           profile.save()
       return user