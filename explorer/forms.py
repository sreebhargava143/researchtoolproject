from django import forms


class SearchForm(forms.Form):
    search_term = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Search'}))
