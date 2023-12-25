from django.forms import ModelForm
from .models import Newsletter, Submission, Topic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User  = get_user_model()

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class AddTopicForm(ModelForm):
    class Meta:
        model = Topic
        fields= '__all__'

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields= '__all__'

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields= '__all__'

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check me-2 nic-search', 'placeholder': 'Search'}))
