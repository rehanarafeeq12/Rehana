from django.http import HttpResponse
from django.shortcuts import redirect, render

from Fest_app.forms import ContestFilterForm, contactform, feedback_form
from Fest_app.models import Student, achievements, contest, feedbacks, gallery, guests, history, judges, management, participant, performer, programmes, result, teachers, venue, volunteers, year
from datetime import datetime
current_year=datetime.now().year

def contestlist(request):
    data=contest.objects.filter(Contest_year=Student.Academic_year)
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
    data=judges.objects.all()
    return render(request,'judges_list.html',{'data':data})

def resultlist(request):
    
    data=result.objects.all()
    return render(request,'result.html',{'data':data})


def guestlist(request):
   
    data=guests.objects.all()
    return render(request,'guest.html',{'data':data})

def programlist(request):
    data=performer.objects.all()
    return render(request,'program.html',{'data':data})

def venue_vol(request):
    vn=venue.objects.all()
    vl=volunteers.objects.all()
    return render(request,'venue_vol.html',{'vn':vn,'vl':vl})

def photoshop(request):
    data=gallery.objects.all()
    return render(request,'photoshop.html',{'data':data})

def school_achievements(request):
    
    data=achievements.objects.all()
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
            form.save()
            return redirect('homepage')
    return render(request,'feedback_add.html',{'form':form})

def feedbacks_view(request):
    data=feedbacks.objects.all()
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

def school_history(request):
    data=history.objects.all()
    return render(request,'history.html',{'data':data})

def explorepage(request):
    data=contest.objects.all()
    Gallery=gallery.objects.all()
    Programmes=programmes.objects.all()
    Result=result.objects.all()
    Guest=guests.objects.all()
    History=history.objects.all()
    context={
        'data':data,
        'Gallery':Gallery,
        'Programmes':Programmes,
        'Result':Result,
        'Guest':Guest,
        'History':History

   }
    return render(request,'explore.html',context)