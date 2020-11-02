from django.shortcuts import render, redirect
from users.models import User, Member, HoodAdmin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from users.decorators import member_required
# Create your views here.

def index(request):
    return render(request, 'welcome.html')

@user_passes_test(lambda  u: u.is_superuser)
def admin_profile(request):
    users = User.objects.all().order_by('id')
    context = {
        'users': users
    }

    return render(request, 'hood/admin_profile.html', context)

@user_passes_test(lambda  u: u.is_superuser)
def make_hood_admin(request, id):
    user = User.objects.get(pk=id)
    user.is_hood_admin = True
    user.save()
    return redirect('admin_pr')

@method_decorator(login_required, name='dispatch')
class BusinessCreateView(UserPassesTestMixin, CreateView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']

    
    def form_valid(self, form):
        print('great')
        form.instance.user = self.request.user
        return super().form_valid(form)

