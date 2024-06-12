from django import forms

from . models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'review', 'profile_picture']

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Bio',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    review = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Mendimi juaj per faqen',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)
