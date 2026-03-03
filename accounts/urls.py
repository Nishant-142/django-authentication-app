from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('approve/<int:id>/', views.approve_user, name='approve_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('update/<int:id>/', views.update_user, name='update_user'),
]