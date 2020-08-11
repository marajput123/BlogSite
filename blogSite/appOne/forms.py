from django.contrib.auth.models import User
from django import forms
from .models import Comment, Post



class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control' ,
                                                                        'id':'register-form'}))
    username= forms.CharField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
                                                                                'id':'register-form'}))
    email = forms.EmailField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
                                                                                'id':'register-form'}))
    first_name = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
                                                                                'id':'register-form'}))
    last_name = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
                                                                                'id':'register-form'}))
    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password")

class CommentForm(forms.ModelForm):
    # author = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
    #                                                                             'id':'register-form'}))
    com_content = forms.CharField(help_text=False, widget=forms.Textarea(attrs={'class':'form-control',
                                                                                'id':"exampleFormControlTextarea1"}))
    class Meta:
        model = Comment
        fields = ('com_content',)

class PostForm(forms.ModelForm):
    title = forms.CharField(help_text=False, widget=forms.TextInput(attrs={'class':'form-control' ,
                                                                                 'id':'register-form'}))
    content = forms.CharField(help_text=False, widget=forms.Textarea(attrs={'class':'form-control',
                                                                                'id':"exampleFormControlTextarea1"}))

    class Meta:
        model = Post
        fields = ('title','content')
