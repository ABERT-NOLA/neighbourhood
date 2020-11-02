from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import (MemberSignup, MemberUpdateForm)
from django.contrib.auth.decorators import login_required
from .models import Member, User
from django.views.generic import CreateView
from .decorators import member_required

# Create your views here.
def index(request):
    return render(request, 'users/welcome.html')



class MemberSignupView(CreateView):
    model = User
    form_class = MemberSignup
    template_name = 'users/member_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hood_member'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        messages.success(self.request, f'Account created')

        return redirect('welcome')

@member_required
def member_profile(request):
    member = request.user
    member_profile = Member.objects.filter(pk=member).first()
    if request.method == 'POST':
        profile_form = MemberUpdateForm(request.POST, request.FILES, instance=member_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Profile successfully updated')
            return redirect('member_profile')
    else:
        profile_form = MemberUpdateForm(instance=member_profile)

    content = {
        'form': profile_form,
        'member': member
    }
    return render(request, 'users/member_profile.html', content)
