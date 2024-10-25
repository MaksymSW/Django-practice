from django import forms
from django.forms import ModelForm, CharField, TextInput, DateField, Textarea
from .models import Tag, Author, Quote


class TagForm(ModelForm):
    name = CharField(
        min_length=3,
        max_length=50, required=True,
        widget=TextInput(attrs={"class": "form-control custom-border", "placeholder": "Enter a tag"})
    )
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(
        min_length=3,
        max_length=50,
        required=True,
        widget=TextInput(attrs={"class": "form-control custom-border", "placeholder": "Example: Roy Smith"})
    )

    born_date = CharField(
        min_length=3,
        max_length=50,
        required=True,
        widget=TextInput(attrs={"class": "form-control custom-border", "placeholder": "month dd, yyyy"})
    )
    
    # born_date1 = DateField(
    #     required=True,
    #     widget=TextInput(attrs={"type": "date", "class": "form-control custom-border"})
    # )
    
    born_location = CharField(
        min_length=3,
        max_length=150,
        required=True,
        widget=TextInput(attrs={"class": "form-control custom-border", "placeholder": "City, Country"})
    )
    
    
    description = CharField(
        required=True,
        widget=Textarea(attrs={"class": "form-control custom-border", "placeholder": "Add a description..."})
    )


    # description1 = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(attrs={"class": "form-control custom-border", "placeholder": "Add a description..."})
    # )

    
    class Meta:
        model = Author
        fields = ['fullname','born_date','born_location','description']


class QuoteForm(ModelForm):

    # quote = TextInput()

    quote = CharField(
        required=True,
        widget=Textarea(attrs={"class": "form-control custom-border", "placeholder": "Add a quote..."})
    )

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['tags','author']
