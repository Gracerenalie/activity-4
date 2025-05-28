from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        confirm = request.POST.get('confirm', '').strip()

        if not username or not password or not confirm:
            return render(request, 'signup.html', {
                'error': 'All fields are required.'
            })

        if password != confirm:
            return render(request, 'signup.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                'error': 'Username already taken.'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('list_students')

    return render(request, 'signup.html')

@login_required()
def list_students(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

@login_required()
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')  # optional
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        year_level = request.POST.get('year_level')

        # You may add validation logic here
        if not first_name or not last_name:
            return render(request, 'add_student.html', {
                'error_message': 'First and Last name are required.',
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'gender': gender,
                'date_of_birth': date_of_birth,
                'year_level': year_level
            })

        Student.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            year_level=year_level
        )
        return redirect('list_students')

    return render(request, 'add.html')



@login_required()
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        # other fields...

        # You can add validation here

        student.first_name = first_name
        student.middle_name = middle_name
        student.last_name = last_name
        # update other fields...
        student.save()
        return redirect('list_students')

    context = {
        'student': student,
        'first_name': student.first_name,
        'middle_name': student.middle_name,
        'last_name': student.last_name,
        # other fields...
    }
    return render(request, 'edit.html', context)

@login_required()
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'delete.html', {'student': student})

