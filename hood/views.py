from django.shortcuts import render, redirect
from users.models import User, Member, HoodAdmin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from users.decorators import member_required, hood_admin_required
from .decorators import admin_required
from .models import Business, Neighbourhood, Post, Comment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    neihbourhood = Neighbourhood.objects.all()
    business = Business.objects.all()

    return render(request, 'welcome.html')

@member_required
def member_index(request):
    posts = Post.objects.all()
    neighbourhoods = Neighbourhood.objects.all()
    user = request.user
    memb_hood = ''
    for neigh in neighbourhoods:
        if neigh.location == user.member.location:
            memb_hood = neigh
    business = Business.objects.get(neighbourhood=memb_hood)
    print(business)
    content = {
        'posts': posts,
        'hood' : memb_hood,
        'business': business
    }
    return render(request, 'hood/member_wel.html', content)
    

@user_passes_test(lambda  u: u.is_superuser)
def admin_profile(request):
    users = User.objects.all().order_by('id')
    neihbourhood = Neighbourhood.objects.all()
    business = Business.objects.all()

    context = {
        'users': users,
        'hoods': neihbourhood,
        'business': business
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
             
    def test_func(self):
        return True 

    def form_valid(self, form):
        print('great')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content', 'image']

    def form_valid(self, form):
        print('great')
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


@member_required
def like_post(request, id):
    post = Post.objects.get(pk=id)
    post.likes += 1
    post.save()
    return redirect('welcome-index')

@member_required
def leave_comment(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        content = request.POST.get('comment')
        comment_inst = Comment(content=content, post_id=id)      
        comment_inst.save()  
        return redirect('welcome-index')