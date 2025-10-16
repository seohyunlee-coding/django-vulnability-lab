from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(label='메시지', widget=forms.Textarea, required=False)


class NoteForm(forms.Form):
    text = forms.CharField(label='노트', widget=forms.Textarea)
