from django import forms


class SearchForm(forms.Form):

    git_nickname = forms.CharField(max_length=50,
                                   label='Search by author name',
                                   required=True
                                   )
