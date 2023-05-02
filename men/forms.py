from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class AddQuestionForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Question
        fields = ['question_text', 'cat']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 5}),
        }


class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'question']
        widgets = {
            'answer_text': forms.Textarea(attrs={'rows': 5}),
            'question': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id', None)
        super().__init__(*args, **kwargs)
        if question_id:
            self.fields['question'].initial = question_id


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))

