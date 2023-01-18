from imaplib import _Authenticator
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.

def index(request):
    return render(request,'index.html')

def userhome(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    return render(request,'userhome.html')

def companyhome(request):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    return render(request,'companyhome.html')

def adminhome(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    return render(request,'adminhome.html')


def userlogin(request):
    error = ""
    error1=""
    if request.method=='POST' and 'sign_up' in request.POST:
        fname=request.POST['fname']
        contact=request.POST['contact']
        email=request.POST['email']
        pas=request.POST['password']
        try:
            user=User.objects.create_user(first_name=fname,last_name=fname,username=email,password=pas)
            Students.objects.create(user=user,phoneNo=contact,type="student")
            error="no"
        except:
            error="yes"

    if request.method=='POST' and 'sign_in' in request.POST:
        uname=request.POST['uemail']
        upas=request.POST['upassword']
        auser=authenticate(username=uname,password=upas)
        if auser:
            try:
                user1=Students.objects.get(user=auser)
                if user1.type=="student":
                    login(request,auser)
                    error1="No"
                else:
                    error1="Yes"
            except:
                error1="Yes"
        else:
            error1="Yes"

    d = {'error':error,'error1':error1}

    return render(request,'userlogin.html',d)

def ALogout(request):
    logout(request)
    return redirect('index')

def CLogout(request):
    logout(request)
    return redirect('index')

def ULogout(request):
    logout(request)
    return redirect('index')


def companylogin(request):
    error = ""
    error1=""
    if request.method=='POST' and 'sign_up' in request.POST:
        fname=request.POST['fname']
        contact=request.POST['contact']
        email=request.POST['email']
        pas=request.POST['password']
        com=request.POST['cname']
        try:
            user=User.objects.create_user(first_name=fname,last_name=fname,username=email,password=pas)
            Company.objects.create(user=user,company=com,phoneNo=contact,type="company",status="pending")
            error="no"
        except:
            error="yes"

    if request.method=='POST' and 'sign_in' in request.POST:
        uname=request.POST['uemail']
        upas=request.POST['upassword']
        auser=authenticate(username=uname,password=upas)
        if auser:
            try:
                user1=Company.objects.get(user=auser)
                if user1.type=="company" and user1.status!="pending":
                    login(request,auser)
                    error1="No"
                else:
                    error1="not"
            except:
                error1="Yes"
        else:
            error1="Yes"

    d = {'error':error,'error1':error1}

    return render(request,'companylogin.html',d)


def adminlogin(request):
    error =""
    if request.method=='POST':
        uname=request.POST['uemail']
        upas=request.POST['upassword']
        user=authenticate(username=uname,password=upas)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'adminlogin.html',d)

def viewUser(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Students.objects.all()
    d={'data':data}
    return render(request,'viewUser.html',d)

def deleteUser(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student=User.objects.get(id=pid)
    student.delete()
    return redirect('viewUser')

def deleteCompany(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    company=User.objects.get(id=pid)
    company.delete()
    return redirect('allCompany')

def pendingCompany(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='pending')
    d={'data':data}
    return render(request,'pendingCompany.html',d)

def acceptCompany(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='Accept')
    d={'data':data}
    return render(request,'acceptCompany.html',d)

def rejectCompany(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.filter(status='Reject')
    d={'data':data}
    return render(request,'rejectCompany.html',d)

def allCompany(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Company.objects.all()
    d={'data':data}
    return render(request,'allCompany.html',d)

def changeStatus(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    company=Company.objects.get(id=pid)
    if request.method=="POST":
        s=request.POST['status']
        company.status=s
        try:
            company.save()
            error="no"
        except:
            error="yes"
    d={'company':company,'error':error}
    return render(request,'changeStatus.html',d)

def addJob(request):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    error=""
    if request.method=='POST':
        title=request.POST['jtitle']
        stdate=request.POST['sdate']
        endate=request.POST['edate']
        salary=request.POST['salary']
        loca=request.POST['location']
        ex=request.POST['experience']
        des=request.POST['description']
        sk=request.POST['skill']
        user=request.user
        company=Company.objects.get(user=user)
        try:
            Jobs.objects.create(company=company,startDate=stdate,endDate=endate,title=title,salary=salary,description=des,experience=ex,location=loca,skills=sk,creationDate=date.today())
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'addJob.html',d)

def jobList(request):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    user=request.user
    company=Company.objects.get(user=user)
    job=Jobs.objects.filter(company=company)
    d={'job':job}
    return render(request,'jobList.html',d)

def deleteJob(request,pid):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    job=Jobs.objects.get(id=pid)
    job.delete()
    return redirect('jobList')

def editJob(request,pid):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    error=""
    job=Jobs.objects.get(id=pid)
    if request.method=='POST':
        title=request.POST['jtitle']
        stdate=request.POST['sdate']
        endate=request.POST['edate']
        salary=request.POST['salary']
        loca=request.POST['location']
        ex=request.POST['experience']
        des=request.POST['description']
        sk=request.POST['skill']
        
        job.title=title
        job.salary=salary
        job.experience=ex
        job.location=loca
        job.skills=sk
        job.description=des

        try:
            job.save()
            error="no"
        except:
            error="yes"
        if stdate:
            try:
                job.startDate=stdate
                job.save()
            except:
                pass
        else:
            pass

        if endate:
            try:
                job.endDate=endate
                job.save()
            except:
                pass
        else:
            pass
    d = {'error':error,'job':job}
    return render(request,'editJob.html',d)


def latestJobList(request):
    job=Jobs.objects.all()
    d={'job':job}
    return render(request,'latestJobList.html',d)

def userLatestJob(request):
    job=Jobs.objects.all().order_by('-startDate')
    user=request.user
    student=Students.objects.get(user=user)
    data=applyJob.objects.filter(student=student)
    li=[]
    for i in data:
        li.append(i.job.id)
    d={'job':job,'li':li}
    return render(request,'userLatestJob.html',d)

def jobDetails(request,pid):
    job=Jobs.objects.get(id=pid)
    d={'job':job}
    return render(request,'jobDetails.html',d)

def applyForJob(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    user=request.user
    student=Students.objects.get(user=user)
    job=Jobs.objects.get(id=pid)
    date1=date.today()
    if job.endDate<date1:
        error="close"
    elif job.startDate>date1:
        error="notopen"
    else:
        if request.method=='POST':
            file=request.FILES['resume']
            applyJob.objects.create(job=job,student=student,resume=file,applyDate=date.today())
            error="done"
    d={'error':error}
    return render(request,'applyForJob.html',d)

def appliedCandiate(request):
    if not request.user.is_authenticated:
        return redirect('companylogin')
    data=applyJob.objects.all()
    d={'data':data}
    return render(request,'appliedCandiate.html',d)