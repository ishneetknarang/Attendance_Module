"""student_attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from student import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.log_in_faculty),
    url(r'^login/', views.log_in_faculty),
    url(r'^logout/', views.log_out_faculty),
    url(r'^save_attendance/', views.save_attendance),
    url(r'^show_attendance_by_date/', views.show_attendance_by_date),
    url(r'^show_attendance_by_student/', views.show_attendance_by_student),
    url(r'^show_attendance_summary/', views.show_attendance_summary),
    url(r'^student_details/1/(?P<student_id>\d+)/$',views.student_details,name='urlname'),
]
