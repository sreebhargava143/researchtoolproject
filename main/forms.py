from django.forms import ModelForm
from django import forms
from main.models import StoryCard, Story


class CardForm(ModelForm):
    story = forms.ModelChoiceField(queryset=Story.objects.none())
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['story'].queryset = Story.objects.filter(author=request.user.id)
    #
    class Meta:
        model = StoryCard
        fields = ('story', 'card_data')
