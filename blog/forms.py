from django import forms

from .models import CommentModel



class CommentsForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        
        exclude=['post']
        labels={
            'user_name':'Full Name',
            'user_email': 'E-mail',
            'text':'Comment',
        }