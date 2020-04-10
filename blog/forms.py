from django import forms
from . models import WriteBlog


class WriteBlogForm(forms.ModelForm):
    title     = forms.CharField(widget= forms.Textarea(attrs={'rows':1, 'cols':70}))
    content   = forms.CharField(widget = forms.Textarea(attrs={'cols':90})) 


    class Meta:
      model = WriteBlog 
      fields = ('title','category','content')

        