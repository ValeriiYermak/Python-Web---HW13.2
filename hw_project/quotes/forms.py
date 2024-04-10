from django import forms
from .models import Author, Quote
from django import forms
from .models import Author, Quote, Tag


class AuthorForm(forms.ModelForm):
    new_author = forms.CharField(label='New Author', required=False)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'born_date': forms.DateInput(attrs={'class': 'form-control'}),
            'born_location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update({'class': 'form-control'})


class QuoteForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    widget=forms.Select(
                                        attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.SelectMultiple(
                                              attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']
        widgets = {'quote': forms.TextInput(attrs={'class': 'form-control'}),
                   }
