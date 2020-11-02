from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='welcome'),
    path('admin_pr/', views.admin_profile, name = 'admin_pr'),
    path('<int:id>/make_admin/', views.make_hood_admin, name = "make_hood_admin"),
    path('reg_business/', views.BusinessCreateView.as_view(), name='register-business'),
    path('reg_hood/', views.HoodCreateView.as_view(), name='register-hood'),
    path('create_post/', views.PostCreateView.as_view(), name='create-post'),

]