from django import forms

from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.TextInput)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    question = forms.IntegerField

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
