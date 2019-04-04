from django import forms
from django.contrib.auth import models as auth_models

from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.TextInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = auth_models.User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password'])
        return user
