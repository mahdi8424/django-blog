from django import forms
from .models import Comment

"""
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, error_messages={
        "required":"First name must not be empty",
        "max_length":"Please use a short name"
    })
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(label="Your Message", widget=forms.Textarea, max_length=500)
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "name":"Your Name",
            "email":"Your Email",
            "text" : "Your Comment"
        }
