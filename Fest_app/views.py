from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages, auth
from Fest_app.forms import SchoolReg, UserReg, StudentReg
from Fest_app.models import School, Student

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')
def homepage(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect ('main_admin')
        elif user is not None and user.is_School:
            if user.school.approval_status==1:
                login(request,user)
                return redirect('admin1page')
        elif user is not None and user.is_Student:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,'Not a Registered User')            
    return render(request,'login.html')

def yearloginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_Year:
            login(request,user)
            return redirect('adminpage')
    return render(request,'login_year.html')

def registerpage(request):
    return render(request,'register.html')

def main_admin(request):
    return render(request,'main_admin.html')

def schoolregister(request):
    user_form=UserReg()
    school_form=SchoolReg()
    if request.method=='POST':
        user_form=UserReg(request.POST)
        school_form=SchoolReg(request.POST)
        if user_form.is_valid() and school_form.is_valid():
            user=user_form.save(commit=False)
            user.is_School=True
            user.save()
            school=school_form.save(commit=False)
            school.user=user
            school.save()
            messages.info(request,'School Registered Successfully')
            return redirect('loginpage')
    return render(request,'schoolregister.html',{'user_form':user_form,'school_form':school_form})

def studentregister(request):
    user_form=UserReg()
    stud_form=StudentReg()
    if request.method=='POST':
        user_form=UserReg(request.POST)
        stud_form=StudentReg(request.POST)
        if user_form.is_valid() and stud_form.is_valid():
            user=user_form.save(commit=False)
            user.is_Student=True
            user.save()
            stud=stud_form.save(commit=False)
            stud.user=user
            stud.save()
            messages.info(request,'Student Registered successfully')
            return redirect('loginpage')
    return render(request,'studentregister.html',{'user_form':user_form,'stud_form':stud_form})

def school_view(request):
    data=School.objects.all()
    return render(request,'school_view.html',{'data':data})

def approve_school(request,id):
    school=School.objects.get(user_id=id)
    school.approval_status=True
    school.save()
    return redirect('school_view')

def student_view(request):
    data=Student.objects.all()
    return render(request,'student_view.html',{'data':data})

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('loginpage')
    return redirect('loginpage')

def explore(request):
    
    return render(request,'index2.html')
