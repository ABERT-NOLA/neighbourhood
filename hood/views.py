from django.shortcuts import render, redirect
from users.models import User, Member, HoodAdmin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from users.decorators import member_required, hood_admin_required
from .decorators import admin_required
from .models import Business, Neighbourhood, Post
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

    def test_func(self):
        return True  

    def form_valid(self, form):
        print('great')
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class BusinessUpdateView(UserPassesTestMixin, UpdateView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']

    def test_func(self):
        return True  

    def form_valid(self, form):
        print('great')
        form.instance.user = self.request.user
        return super().form_valid(form)

class BusinessDetailView(DetailView):
    model = Business

@method_decorator(login_required, name='dispatch')
class BusinessDeleteView(UserPassesTestMixin, DeleteView):
    model = Business
    fields = ['name', 'email', 'desc', 'neighbourhood']
    success_url = '/'

   
@method_decorator(admin_required, name='dispatch')
class HoodCreateView(UserPassesTestMixin, CreateView):
    model = Neighbourhood
    fields = '__all__'      

    def test_func(self):
        return True    

    def form_valid(self, form):
        return super().form_valid(form)


class HoodDetailView(DetailView):
    model = Neighbourhood

@method_decorator(admin_required, name='dispatch')
class HoodUpdateView(UserPassesTestMixin, UpdateView):
    model = Neighbourhood
    fields = '__all__'
               
    def test_func(self):
        return True  
        
    def form_valid(self, form):
        print('great')
        return super().form_valid(form)

@method_decorator(admin_required, name='dispatch')
class HoodDeleteView(UserPassesTestMixin, DeleteView):
    model = Neighbourhood
    fields = '__all__'
    success_url = '/'
             

    def form_valid(self, form):
        print('great')
        return super().form_valid(form)

@method_decorator(member_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content', 'image']

    def form_valid(self, form):
        print('great')
        print(self.request.user.userprofile.neighbourhood)
        form.instance.neighbourhood = self.request.user.userprofile.neighbourhood
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post