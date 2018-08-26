from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from datetime import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def log_in_faculty(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    if request.user:
        if not Attendance.objects.filter(date = date.today()):
            students = Student.objects.all()
            return render(request, 'attendance.html', {'status': 'login', 'students': students, })
        else:
            msg = 'Attendance done already !!!'
            return render(request, 'attendance.html', {'status': 'login', 'msg': msg, })

    elif request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                emp = Faculty.objects.get(faculty=request.user)
                if emp is not None:
                    request.session['faculty_user']= username
                    students = Student.objects.all()
                    messages.info(request,'Successfully login '+emp.faculty.first_name)
                    return render( request, 'attendance.html',{'status': 'login','students':students,})
            else:
                messages.error( request, ' Invalid username and password ' )
                return HttpResponseRedirect('/')
        else:
            messages.error( request, ' Invalid username and password ' )
            return HttpResponseRedirect( '/' )
    form = LogInForm()
    return render( request, 'login.html', {'status': 'logout', 'form': form} )


def log_out_faculty(request):
    print('logout')
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/login/')

def save_attendance(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':
        present_list = request.POST.getlist('status')
        students = Student.objects.all().order_by('student_id')
        for student in students:
            if student.student_id in present_list:
                att_obj = Attendance(student = student,status = 1)
            else:
                att_obj = Attendance(student = student, status = 0)
            att_obj.save()
        messages.success(request,'Attendance done')
    return HttpResponseRedirect('/home/')


def show_attendance_by_date(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':  # datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
        date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
        students = Attendance.objects.filter(date=date).order_by('student')
        return render(request, 'attendance_details.html', {'students': students, })
    return render(request, 'attendance_details.html')


def show_attendance_by_student(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':
        form = StudentLookUpForm(request.POST)
        student = request.POST.get('student')
        attendances = Attendance.objects.filter(student=student).order_by('-date')
        return render(request, 'attendance_by_student.html', {'attendances': attendances,'form': form,})
    form = StudentLookUpForm()
    return render(request, 'attendance_by_student.html',{'form':form,})


def show_attendance_summary(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':
        form = DateRangeForm(request.POST)
        date_range = request.POST.get('date')
        date_range = list(date_range.split(' - '))
        dates_list = []
        dates_list.extend([datetime.strptime(date_range[0], '%d/%m/%Y').date(),datetime.strptime(date_range[1], '%d/%m/%Y').date()])
        date_range = tuple(dates_list)
        print('date_range:::::::',date_range )

        attendances = Attendance.objects.filter(date__range=date_range, status=1).order_by('student')
        students = Student.objects.all()
        print('attendances',str(attendances))
        attendance_dict ={}
        for attendance in attendances:
            if attendance.student in attendance_dict:
                attendance_dict.update(
                    {attendance.student:attendance_dict[attendance.student]+1})
            else:
                attendance_dict.update(
                    {attendance.student : 1})

        return render(request, 'attendance_summary.html', {'students': students,
                                                           'attendance_dict': attendance_dict,
                                                           'form': form, })
    form = DateRangeForm()
    return render(request, 'attendance_summary.html', {'form': form})

def student_details(request,student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'POST':
        form = StudentLookUpForm(request.POST)
        student = request.POST.get('student')
        #attendances = Attendance.objects.filter(student=student).order_by('-date')
        return render(request,'student_detail.html',{'student':student})
    student=Student.objects.get(pk=student_id)
    return render(request,'student_detail.html',{'student':student})

    