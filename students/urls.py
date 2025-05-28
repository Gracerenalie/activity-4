from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', csrf_exempt(LogoutView.as_view(next_page='login')), name='logout'),
    path('signup/', views.signup, name='signup'),
]
