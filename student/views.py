from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from datetime import *
from .forms import *
from django.contrib import messages


def log_in_faculty(request):
    if 'faculty_user' in request.session and request.session['faculty_user'] != '':
        currentdate=date.today() 
        att_obj=Attendance.objects.filter(date=currentdate)
        if att_obj:
            pass
        else :
            students = Student.objects.all()
            return render(request, 'attendance.html', {'status': 'login', 'students': students, })
        message="Attendance is already taken"
        return render(request, 'attendance.html', {'status': 'login', 'message': message, })

    # elif request.method == 'POST':
    #     form = LogInForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         emp = list(Faculty.objects.filter(username=username,password=password))
    #         if len(emp) > 0:
    #             print( username, password,repr(emp[0]) )
    #             request.session['faculty_user']= username
    #             currentdate=date.today()
    #             att_obj=Attendance.objects.filter(date=currentdate)

    #             if att_obj:
    #                 pass
    #             else :
    #                 students = Student.objects.all()
    #                 return render(request, 'attendance.html', {'status': 'login', 'students': students, })
    #             message="Attendance is already taken"
    #             messages.info(request,'Successfully login '+emp[0].first_name)
    #             return render(request, 'attendance.html', {'status': 'login', 'message': message, })
    #         else:
    #             messages.error( request, ' Invalid username and password ' )
    #             return HttpResponseRedirect('/')
    #     else:
    #         messages.error( request, ' Invalid username and password ' )
    #         return HttpResponseRedirect( '/' )
    else:
        form = LogInForm()
        return render( request, 'login.html', {'status': 'logout', 'form': form} )


def log_out_faculty(request):
    form = LogInForm()
    request.session['faculty_user'] = ''
    return render( request, 'login.html',{'status': 'logout','form':form } )


def save_attendance(request):
    if request.method == 'POST':
        present_list = request.POST.getlist('status')
        students = Student.objects.all().order_by('student_id')
        for student in students:
            if student.student_id in present_list:
                att_obj = Attendance(student = student,status = 1)
            else:
                att_obj = Attendance(student = student, status = 0)
            att_obj.save()
        messages.success(request,'Attendance done')
    return HttpResponseRedirect('/login/')


def show_attendance_by_date(request):
    if request.method == 'POST':  # datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
        date = datetime.strptime(request.POST.get('date'), "%Y-%m-%d").date()
        students = Attendance.objects.filter(date=date).order_by('student')
        return render(request, 'attendance_details.html', {'students': students, })
    return render(request, 'attendance_details.html')


def show_attendance_by_student(request):
    if request.method == 'POST':
        form = StudentLookUpForm(request.POST)
        student = request.POST.get('student')
        attendances = Attendance.objects.filter(student=student).order_by('-date')
        return render(request, 'attendance_by_student.html', { 'attendances': attendances,'form':form, })
    form = StudentLookUpForm()
    return render(request, 'attendance_by_student.html',{'form':form,})


def show_attendance_summary(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        date_range =request.POST.get('date')
        date_range = list(date_range.split(' - '))
        dates_list = []
        dates_list.extend([datetime.strptime(date_range[0], '%d/%m/%Y').date(),datetime.strptime(date_range[1], '%d/%m/%Y').date()])
        date_range = tuple(dates_list)

        attendances = Attendance.objects.filter(date__range=date_range,status=True).order_by('student')
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

        return render(request, 'attendance_summary.html', {'students': students,'attendance_dict':attendance_dict,'form':form,})
    form = DateRangeForm()
    return render(request, 'attendance_summary.html',{'form':form})

def student_details(request,student_id):
    student=Student.objects.get(pk=student_id)
    return render(request,'student_detail.html',{'student':student})
