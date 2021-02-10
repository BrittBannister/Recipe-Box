from django import forms
from recipe_app.models import Author 

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)

# class AddAuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = [
#             'name',
#             'bio',
#         ]

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput) 
