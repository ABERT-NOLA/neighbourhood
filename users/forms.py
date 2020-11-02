from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, User
from crispy_forms.helper import FormHelper
from django.db import transaction

class MemberSignup(UserCreationForm):
    location = forms.CharField(max_length=100, label='Location',widget=forms.TextInput(attrs={'placeholder':'100 abc street'}))
    contact = forms.CharField( label='Phone Number',widget=forms.TextInput(attrs={'placeholder':'075358901'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'location', 'contact', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hood_member = True        
        user.save()
        print(user)
        location = self.cleaned_data.get('location')
        phone = self.cleaned_data.get('contact')

        member = Member.objects.create(
            user=user, 
            location= location,
            contact = phone,
            )
        member.save()
        return user

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['location', 'contact', 'image']