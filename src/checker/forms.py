from django import forms


class AnsForm(forms.Form):

    ans_section     = forms.CharField(label='',widget=forms.Textarea) 
