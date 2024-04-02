from django import forms
from django.contrib.auth.forms import UserCreationForm

from Fest_app.models import School, Student, User, achievements, contact, contest, feedbacks, gallery, guests, history, judges, management, participant, performer, programmes, result, school_photoes, teachers, venue, volunteers, year

class DateInput(forms.DateInput):
    input_type='date'


class UserReg(UserCreationForm):
    username=forms.EmailField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password1','password2')

class SchoolReg(forms.ModelForm):
    class Meta:
        model=School
        exclude=('user','approval_status')
class StudentReg(forms.ModelForm):
    DOB=forms.DateField(widget=DateInput)
    class Meta:
        model=Student
        exclude=('user',)
class contest_list(forms.ModelForm):
    class Meta:
        model=contest
        exclude=('user','Contest_year')
class participant_list(forms.ModelForm):
    class Meta:
        model=participant
        exclude=('user',)
class judges_list(forms.ModelForm):
    class Meta:
        model=judges
        exclude=('user',)
class result_list(forms.ModelForm):
    class Meta:
        model=result
        exclude=('user',)
class programmes_list(forms.ModelForm):
    class Meta:
        model=programmes
        exclude=('user',)
class performers_list(forms.ModelForm):
    class Meta:
        model=performer
        exclude=('user',)
class venue_list(forms.ModelForm):
    class Meta:
        model=venue
        exclude=('user',)
class volunteers_list(forms.ModelForm):
    class Meta:
        model=volunteers
        exclude=('user',)
class guests_form(forms.ModelForm):
    class Meta:
        model=guests
        exclude=('user',)
class gallery_form(forms.ModelForm):
    class Meta:
        model=gallery
        exclude=('user',)
class achievements_form(forms.ModelForm):
    class Meta:
        model=achievements
        exclude=('user',)
class management_form(forms.ModelForm):
    class Meta:
        model=management
        fields='__all__'
class teachers_form(forms.ModelForm):
    class Meta:
        model=teachers
        fields='__all__'
        
class feedback_form(forms.ModelForm):
    class Meta:
        model=feedbacks
        exclude=('user',)
   
class contactform(forms.ModelForm):
    class Meta:
        model=contact
        exclude=('user',)

class ContestFilterForm(forms.Form):
    Contest_Name=forms.CharField()

class yearform(forms.ModelForm):
    Year=forms.DateField(widget=DateInput)
    class Meta:
        model=year
        exclude=('user',)

class historyform(forms.ModelForm):
    class Meta:
        model=history
        fields='__all__'

class photoform(forms.ModelForm):
    class Meta:
        model=school_photoes
        fields='__all__'


        
        

