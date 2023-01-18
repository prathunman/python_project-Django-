"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('userlogin',userlogin,name="userlogin"),
    path('userhome',userhome,name="userhome"),
    path('CLogout',CLogout,name="CLogout"),
    path('ALogout',ALogout,name="ALogout"),
    path('ULogout',ULogout,name="ULogout"),
    path('companylogin',companylogin,name="companylogin"),
    path('companyhome',companyhome,name="companyhome"),
    path('adminlogin',adminlogin,name="adminlogin"),
    path('adminhome',adminhome,name="adminhome"),
    path('viewUser',viewUser,name="viewUser"),
    path('deleteUser/<int:pid>',deleteUser,name="deleteUser"),
    path('pendingCompany',pendingCompany,name="pendingCompany"),
    path('acceptCompany',acceptCompany,name="acceptCompany"),
    path('rejectCompany',rejectCompany,name="rejectCompany"),
    path('allCompany',allCompany,name="allCompany"),
    path('changeStatus/<int:pid>',changeStatus,name="changeStatus"),
    path('deleteCompany/<int:pid>',deleteCompany,name="deleteCompany"),
    path('addJob',addJob,name="addJob"),
    path('jobList',jobList,name="jobList"),
    path('deleteJob/<int:pid>',deleteJob,name="deleteJob"),
    path('editJob/<int:pid>',editJob,name="editJob"),
    path('latestJobList',latestJobList,name="latestJobList"),
    path('userLatestJob',userLatestJob,name="userLatestJob"),
    path('jobDetails/<int:pid>',jobDetails,name="jobDetails"),
    path('applyForJob/<int:pid>',applyForJob,name="applyForJob"),
    path('appliedCandiate',appliedCandiate,name="appliedCandiate"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
