

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages, auth
from Fest_app.filters import ContestFilter
from Fest_app.forms import ContestFilterForm,  SchoolReg, UserReg, StudentReg, achievements_form, contactform, contest_list, feedback_form, gallery_form, guests_form, historyform, judges_list, management_form, participant_list, performers_list, photoform, programmes_list, result_list,  teachers_form, venue_list, volunteers_list, yearform
from Fest_app.models import School, Student, achievements, contest, feedbacks, gallery, guests, history, judges, management, participant, performer, programmes, result, school_photoes, teachers, venue, volunteers, year

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


def admin1page(request):
    return render(request,'admin1.html')



def registerpage(request):
    return render(request,'register.html')

def adminpage(request):
    return render(request,'admin.html')

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

def contestadd(request):
    form=contest_list()
    if request.method=='POST':
        form=contest_list(request.POST)
        if form.is_valid():
            contests=form.save(commit=False)
            contests.user=request.user
            contests.save()
            return redirect ('contestadd')
    return render(request,'contestadd.html',{'form':form})


def contestview(request):
    u=request.user
    print(u)
    data=contest.objects.filter(user=u)
    return render(request,'contestview.html',{'data':data}) 

def update_list(request,id):
    data=contest.objects.get(id=id)
    form=contest_list(instance=data)
    if request.method=='POST':
        form=contest_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('contestview')
    return render(request,'contest_update.html',{'form':form})
def del_list(request,id):
    contest.objects.get(id=id).delete()
    return redirect('contestview')

def participant_add(request):
    form=participant_list()
    if request.method=='POST':
        form=participant_list(request.POST)
        if form.is_valid():
            participants=form.save(commit=False)
            participants.user=request.user
            participants.save()
            return redirect ('participant_add')
    return render(request,'participant_add.html',{'form':form})
def participant_view(request):
    u=request.user
    print(u)
    data=participant.objects.filter(user=u)    
    return render(request,'participant_view.html',{'data':data}) 
def update_participant(request,id):
    data=participant.objects.get(id=id)
    form=participant_list(instance=data)
    if request.method=='POST':
        form=participant_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('participant_view')
    return render(request,'participant_update.html',{'form':form})
def del_participant(request,id):
    participant.objects.get(id=id).delete()
    return redirect('participant_view')

def judges_add(request):
    form=judges_list()
    if request.method=='POST':
        form=judges_list(request.POST)
        if form.is_valid():
            judge=form.save(commit=False)
            judge.user=request.user
            judge.save()
            return redirect ('judges_add')
    return render(request,'judges_add.html',{'form':form})
def judges_view(request):
    u=request.user
    print(u)
    data=judges.objects.filter(user=u)  
    return render(request,'judges_view.html',{'data':data}) 
def update_judges(request,id):
    data=judges.objects.get(id=id)
    form=judges_list(instance=data)
    if request.method=='POST':
        form=judges_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('judges_view')
    return render(request,'judges_update.html',{'form':form})
def del_judges(request,id):
    judges.objects.get(id=id).delete()
    return redirect('judges_view')

def result_add(request):
    form=result_list()
    if request.method=='POST':
        form=result_list(request.POST)
        if form.is_valid():
            results=form.save(commit=False)
            results.user=request.user
            results.save()
            return redirect ('result_add')
    return render(request,'result_add.html',{'form':form})
def result_view(request):
    u=request.user
    print(u)
    data=result.objects.filter(user=u)  
    return render(request,'result_view.html',{'data':data}) 
def update_result(request,id):
    data=result.objects.get(id=id)
    form=result_list(instance=data)
    if request.method=='POST':
        form=result_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('result_view')
    return render(request,'result_update.html',{'form':form})
def del_result(request,id):
    result.objects.get(id=id).delete()
    return redirect('result_view')

def programmes_add(request):
    form=programmes_list()
    if request.method=='POST':
        form=programmes_list(request.POST)
        if form.is_valid():
            programm=form.save(commit=False)
            programm.user=request.user
            programm.save()
            return redirect ('programmes_add')
    return render(request,'programmes_add.html',{'form':form})
def programmes_view(request):
    u=request.user
    print(u)
    data=programmes.objects.filter(user=u)  
    return render(request,'programmes_view.html',{'data':data}) 
def update_programmes(request,id):
    data=programmes.objects.get(id=id)
    form=programmes_list(instance=data)
    if request.method=='POST':
        form=programmes_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('programmes_view')
    return render(request,'programmes_update.html',{'form':form})
def del_programmes(request,id):
    programmes.objects.get(id=id).delete()
    return redirect('programmes_view')

def performer_add(request):
    form=performers_list()
    if request.method=='POST':
        form=performers_list(request.POST)
        if form.is_valid():
            performers=form.save(commit=False)
            performers.user=request.user
            performers.save()
            return redirect ('performer_add')
    return render(request,'performer_add.html',{'form':form})
def performer_view(request):
    u=request.user
    print(u)
    data=performer.objects.filter(user=u)  
    return render(request,'performer_view.html',{'data':data}) 
def update_performer(request,id):
    data=performer.objects.get(id=id)
    form=performers_list(instance=data)
    if request.method=='POST':
        form=performers_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('performer_view')
    return render(request,'performer_update.html',{'form':form})
def del_performer(request,id):
    performer.objects.get(id=id).delete()
    return redirect('performer_view')

def venue_add(request):
    form=venue_list()
    if request.method=='POST':
        form=venue_list(request.POST)
        if form.is_valid():
            venues=form.save(commit=False)
            venues.user=request.user
            venues.save()
            return redirect ('venue_add')
    return render(request,'venue_add.html',{'form':form})
def venue_view(request):
    u=request.user
    print(u)
    data=venue.objects.filter(user=u)
    return render(request,'venue_view.html',{'data':data}) 
def update_venue(request,id):
    data=venue.objects.get(id=id)
    form=venue_list(instance=data)
    if request.method=='POST':
        form=venue_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('venue_view')
    return render(request,'venue_update.html',{'form':form})
def del_venue(request,id):
    venue.objects.get(id=id).delete()
    return redirect('venue_view')

def volunteers_add(request):
    form=volunteers_list()
    if request.method=='POST':
        form=volunteers_list(request.POST)
        if form.is_valid():
            vol=form.save(commit=False)
            vol.user=request.user
            vol.save()
            return redirect ('volunteers_add')
    return render(request,'volunteers_add.html',{'form':form})
def volunteers_view(request):
    u=request.user
    print(u)
    data=volunteers.objects.filter(user=u)
    return render(request,'volunteers_view.html',{'data':data}) 
def update_volunteers(request,id):
    data=volunteers.objects.get(id=id)
    form=volunteers_list(instance=data)
    if request.method=='POST':
        form=volunteers_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('volunteers_view')
    return render(request,'volunteers_update.html',{'form':form})
def del_volunteers(request,id):
    volunteers.objects.get(id=id).delete()
    return redirect('volunteers_view')

def guests_add(request):
    form=guests_form()
    if request.method=='POST':
        form=guests_form(request.POST,request.FILES)
        if form.is_valid():
            guest=form.save(commit=False)
            guest.user=request.user
            guest.save()
            return redirect ('guests_add')
    return render(request,'guests_add.html',{'form':form})
def guests_view(request):
    u=request.user
    print(u)
    data=guests.objects.filter(user=u)
    return render(request,'guests_view.html',{'data':data}) 
def update_guests(request,id):
    data=guests.objects.get(id=id)
    form=guests_form(instance=data)
    if request.method=='POST':
        form=guests_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('guests_view')
    return render(request,'guests_update.html',{'form':form})
def del_guests(request,id):
    guests.objects.get(id=id).delete()
    return redirect('guests_view')

def gallery_add(request):
    form=gallery_form()
    if request.method=='POST':
        form=gallery_form(request.POST,request.FILES)
        if form.is_valid():
            galery=form.save(commit=False)
            galery.user=request.user
            galery.save()
            return redirect ('gallery_add')
    return render(request,'gallery_add.html',{'form':form})
def gallery_view(request):
    u=request.user
    print(u)
    data=gallery.objects.filter(user=u)
    return render(request,'gallery_view.html',{'data':data}) 
def update_gallery(request,id):
    data=gallery.objects.get(id=id)
    form=gallery_form(instance=data)
    if request.method=='POST':
        form=gallery_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('gallery_view')
    return render(request,'gallery_update.html',{'form':form})
def del_gallery(request,id):
    gallery.objects.get(id=id).delete()
    return redirect('gallery_view')

def achievements_add(request):
    form=achievements_form()
    if request.method=='POST':
        form=achievements_form(request.POST,request.FILES)
        if form.is_valid():
            achievement=form.save(commit=False)
            achievement.user=request.user
            achievement.save()
            return redirect ('achievements_add')
    return render(request,'achievements_add.html',{'form':form})
def achievements_view(request):
    u=request.user
    print(u)
    data=achievements.objects.filter(user=u)
    return render(request,'achievements_view.html',{'data':data}) 
def update_achievements(request,id):
    data=achievements.objects.get(id=id)
    form=achievements_form(instance=data)
    if request.method=='POST':
        form=achievements_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('achievements_view')
    return render(request,'achievements_update.html',{'form':form})
def del_achievements(request,id):
    achievements.objects.get(id=id).delete()
    return redirect('achievements_view')

def management_add(request):
    form=management_form()
    if request.method=='POST':
        form=management_form(request.POST,request.FILES)
        if form.is_valid():
            managements=form.save(commit=False)
            managements.user=request.user
            managements.save()
            return redirect ('management_add')
    return render(request,'management_add.html',{'form':form})
def management_view(request):
    u=request.user
    print(u)
    data=management.objects.filter(user=u)
    return render(request,'management_view.html',{'data':data}) 
def update_management(request,id):
    data=management.objects.get(id=id)
    form=management_form(instance=data)
    if request.method=='POST':
        form=management_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('management_view')
    return render(request,'management_update.html',{'form':form})
def del_management(request,id):
    management.objects.get(id=id).delete()
    return redirect('management_view')

def teachers_add(request):
    form=teachers_form()
    if request.method=='POST':
        form=teachers_form(request.POST)
        if form.is_valid():
            teacher=form.save(commit=False)
            teacher.user=request.user
            teacher.save()
            return redirect ('teachers_add')
    return render(request,'teachers_add.html',{'form':form})
def teachers_view(request):
    u=request.user
    print(u)
    data=teachers.objects.filter(user=u)
    return render(request,'teachers_view.html',{'data':data}) 
def update_teachers(request,id):
    data=teachers.objects.get(id=id)
    form=teachers_form(instance=data)
    if request.method=='POST':
        form=teachers_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('teachers_view')
    return render(request,'teachers_update.html',{'form':form})
def del_teachers(request,id):
    teachers.objects.get(id=id).delete()
    return redirect('teachers_view')

def history_add(request):
    form=historyform()
    if request.method=='POST':
        form=historyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('history_add')
    return render(request,'history_add.html',{'form':form})
def history_view(request):
   data=history.objects.all()
   return render(request,'history_view.html',{'data':data}) 
def update_history(request,id):
    data=history.objects.get(id=id)
    form=historyform(instance=data)
    if request.method=='POST':
        form=historyform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('history_view')
    return render(request,'history_update.html',{'form':form})
def del_history(request,id):
    history.objects.get(id=id).delete()
    return redirect('history_view')
def school_history(request):
    data=history.objects.all()
    return render(request,'history.html')

def photo_add(request):
    form=photoform()
    if request.method=='POST':
        form=photoform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('photo_add')
    return render(request,'photo_add.html',{'form':form})
def photo_view(request):
   data=school_photoes.objects.all()
   return render(request,'photo_view.html',{'data':data}) 
def update_photo(request,id):
    data=school_photoes.objects.get(id=id)
    form=photoform(instance=data)
    if request.method=='POST':
        form=photoform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('photo_view')
    return render(request,'photo_update.html',{'form':form})
def del_photo(request,id):
    school_photoes.objects.get(id=id).delete()
    return redirect('photo_view')
def school_photo(request):
    data=school_photoes.objects.all()
    return render(request,'photo.html',{'data':data})



def contestlist(request):
    u=request.user
    print(u)
    data=contest.objects.filter(user=u)
    return render(request,'contest_list.html',{'data':data})

def participantlist(request):
    Contest_Name=request.GET.get('Contest_Name')
    participants=participant.objects.all()
    if Contest_Name:
        participants=participants.filter(Contest_Name__icontains=Contest_Name)
    context={
        'form':ContestFilterForm(),
        'data':participants
    }
    return render(request,'participant_lists.html',context)

def judgeslist(request):
    u=request.user
    print(u)
    data=judges.objects.filter(user=u)
    return render(request,'judges_list.html',{'data':data})

def resultlist(request):
    u=request.user
    print(u)
    data=result.objects.filter(user=u)
    return render(request,'result.html',{'data':data})


def guestlist(request):
    u=request.user
    print(u)
    data=guests.objects.filter(user=u)
    return render(request,'guest.html',{'data':data})

def programlist(request):
    u=request.user
    print(u)
    data=performer.objects.filter(user=u)
    return render(request,'program.html',{'data':data})

def venue_vol(request):
    u=request.user
    print(u)
    data=venue.objects.filter(user=u)
    u=request.user
    print(u)
    data=volunteers.objects.filter(user=u)
    return render(request,'venue_vol.html',{'data':data})
def programlist(request):
    u=request.user
    print(u)
    data=programmes.objects.filter(user=u)
    return render(request,'program.html',{'data':data})

def photoshop(request):
    u=request.user
    print(u)
    data=gallery.objects.filter(user=u)
    return render(request,'photoshop.html',{'data':data})

def school_achievements(request):
    u=request.user
    print(u)
    data=achievements.objects.filter(user=u)
    return render(request,'achievements.html',{'data':data})

def tchrs(request):
    data=teachers.objects.all()
    return render(request,'teachers.html',{'data':data})

def mngmnt(request):
    data=management.objects.all()
    return render(request,'management.html',{'data':data})


def feedbacks_add(request):
    form=feedback_form()
    if request.method=='POST':
        form=feedback_form(request.POST)
        if form.is_valid():
            feedback=form.save(commit=False)
            feedback.user=request.user
            feedback.save()
            return redirect('homepage')
    return render(request,'feedback_add.html',{'form':form})

def feedbacks_view(request):
    u=request.user
    print(u)
    data=feedbacks.objects.filter(user=u)
    return render(request,'feedback_view.html',{'data':data}) 

def aboutpage(request):
    return render(request,'about.html')

def supportpage(request):
    return render(request,'support.html')

def contactpage(request):
    form=contactform()
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.user=request.user
            contact.save()
            return redirect('success')
    return render(request,'contact.html',{'form':form})
def success(request):
    return HttpResponse("Success!")
    return render(request,'participant_lists.html',{'queryset':filtered_queryset})  

def year_add(request):
    form1=UserReg()
    form=yearform()
    if request.method=='POST':
        form1=UserReg(request.POST)
        form=yearform(request.POST)
        if form1.is_valid() and form.is_valid():
            user=form1.save(commit=False)
            user.is_Year=True
            user.save()
            Year=form.save(commit=False)
            Year.user=user
            Year.save()
            return redirect ('year_add')
    return render(request,'year_add.html',{'form1':form1,'form':form})
def year_view(request):
    data=year.objects.all()
    return render(request,'year_view.html',{'data':data}) 
def Yearpage(request):
    data=year.objects.all()
    return render(request,'year.html',{'data':data}) 

def homepage1(request,id):
    Contest=contest.objects.filter(id=id)
    Result=result.objects.filter(id=id)
    Programmes=programmes.objects.filter(id=id)
    Performers=performer.objects.filter(id=id)
    Guests=guests.objects.filter(id=id)
    Gallery=gallery.objects.filter(id=id)
    

    context={
        'Contest':Contest,
        'Result':Result,
        'Programmes':Programmes,
        'Performers':Performers,
        'Guests':Guests,
        'Gallery':Gallery,
       
        
}
    return render(request,'index2.html',context)
# def homepage(request,id):
#     data = contest.objects.filter(id=id)
#     context = {
#         'data':data
#     }
#     return render(request,'index.html',context)

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('loginpage')
    return redirect('loginpage')


