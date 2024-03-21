from django.urls import path

from Fest_app import views


urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('yearloginpage',views.yearloginpage,name='yearloginpage'),
    path('registerpage',views.registerpage,name='registerpage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('schoolregister',views.schoolregister,name='schoolregister'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('main_admin',views.main_admin,name='main_admin'),
    path('school_view',views.school_view,name='school_view'),
    path('approve_school/<int:id>/',views.approve_school,name='approve_school'),
    path('student_view',views.student_view,name='student_view'),
    path('contestadd',views.contestadd,name='contestadd'),
    path('contestview',views.contestview,name='contestview'),
    path('update_list/<int:id>/',views.update_list,name='update_list'),
    path('del_list/<int:id>/',views.del_list,name='del_list'),
    path('participant_add',views.participant_add,name='participant_add'),
    path('participant_view',views.participant_view,name='participant_view'),
    path('update_participant/<int:id>/',views.update_participant,name='update_participant'),
    path('del_participant/<int:id>/',views.del_participant,name='del_participant'),
    path('judges_add',views.judges_add,name='judges_add'),
    path('judges_view',views.judges_view,name='judges_view'),
    path('update_judges/<int:id>/',views.update_judges,name='update_judges'),
    path('del_judges/<int:id>/',views.del_judges,name='del_judges'),
    path('result_add',views.result_add,name='result_add'),
    path('result_view',views.result_view,name='result_view'),
    path('update_result/<int:id>/',views.update_result,name='update_result'),
    path('del_result/<int:id>/',views.del_result,name='del_result'),
    path('programmes_add',views.programmes_add,name='programmes_add'),
    path('programmes_view',views.programmes_view,name='programmes_view'),
    path('update_programmes/<int:id>/',views.update_programmes,name='update_programmes'),
    path('del_programmes/<int:id>/',views.del_programmes,name='del_programmes'),
    path('performer_add',views.performer_add,name='performer_add'),
    path('performer_view',views.performer_view,name='performer_view'),
    path('update_performer/<int:id>/',views.update_performer,name='update_performer'),
    path('del_performer/<int:id>/',views.del_performer,name='del_performer'),
    path('venue_add',views.venue_add,name='venue_add'),
    path('venue_view',views.venue_view,name='venue_view'),
    path('update_venue/<int:id>/',views.update_venue,name='update_venue'),
    path('del_venue/<int:id>/',views.del_venue,name='del_venue'),
    path('volunteers_add',views.volunteers_add,name='volunteers_add'),
    path('volunteers_view',views.volunteers_view,name='volunteers_view'),
    path('update_volunteers/<int:id>/',views.update_volunteers,name='update_volunteers'),
    path('del_volunteers/<int:id>/',views.del_volunteers,name='del_volunteers'),
    path('guests_add',views.guests_add,name='guests_add'),
    path('guests_view',views.guests_view,name='guests_view'),
    path('update_guests/<int:id>/',views.update_guests,name='update_guests'),
    path('del_guests/<int:id>/',views.del_guests,name='del_guests'),
    path('gallery_add',views.gallery_add,name='gallery_add'),
    path('gallery_view',views.gallery_view,name='gallery_view'),
    path('update_gallery/<int:id>/',views.update_gallery,name='update_gallery'),
    path('del_gallery/<int:id>/',views.del_gallery,name='del_gallery'),
    path('achievements_add',views.achievements_add,name='achievements_add'),
    path('achievements_view',views.achievements_view,name='achievements_view'),
    path('update_achievements/<int:id>/',views.update_achievements,name='update_achievements'),
    path('del_achievements/<int:id>/',views.del_achievements,name='del_achievements'),
    path('management_add',views.management_add,name='management_add'),
    path('management_view',views.management_view,name='management_view'),
    path('update_management/<int:id>/',views.update_management,name='update_management'),
    path('del_management/<int:id>/',views.del_management,name='del_management'),
    path('teachers_add',views.teachers_add,name='teachers_add'),
    path('teachers_view',views.teachers_view,name='teachers_view'),
    path('update_teachers/<int:id>/',views.update_teachers,name='update_teachers'),
    path('del_teachers/<int:id>/',views.del_teachers,name='del_teachers'),
    path('history_add',views.history_add,name='history_add'),
    path('history_view',views.history_view,name='history_view'),
    path('update_history/<int:id>/',views.update_history,name='update_history'),
    path('del_history/<int:id>/',views.del_history,name='del_history'),
    path('school_history',views.school_history,name='school_history'),
    path('school_photo',views.school_photo,name='school_photo'),
    path('photo_add',views.photo_add,name='photo_add'),
    path('photo_view',views.photo_view,name='photo_view'),
    path('update_photo/<int:id>/',views.update_photo,name='update_photo'),
    path('del_photo/<int:id>/',views.del_photo,name='del_photo'),
    

    path('contestlist',views.contestlist,name='contestlist'),
    path('participantlist',views.participantlist,name='participantlist'),
    path('judgeslist',views.judgeslist,name='judgeslist'),
    path('resultlist',views.resultlist,name='resultlist'),
    path('guestlist',views.guestlist,name='guestlist'),
    path('programlist',views.programlist,name='programlist'),
    path('venue_vol',views.venue_vol,name='venue_vol'),
    path('photoshop',views.photoshop,name='photoshop'),
    path('school_achievements',views.school_achievements,name='school_achievements'),
    path('tchrs',views.tchrs,name='tchrs'),
    path('mngmnt',views.mngmnt,name='mngmnt'),
    path('feedbacks_add',views.feedbacks_add,name='feedbacks_add'),
    path('feedbacks_view',views.feedbacks_view,name='feedbacks_view'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('supportpage',views.supportpage,name='supportpage'),
    path('success',views.success,name='success'),
    path('year_add',views.year_add,name='year_add'),
    path('admin1page',views.admin1page,name='admin1page'),
    path('year_view',views.year_view,name='year_view'),
    path('Yearpage',views.Yearpage,name='Yearpage'),
    path('homepage',views.homepage,name='homepage'),
    path('logout', views.logout, name='logout'),
    path('homepage1/<int:id>/',views.homepage1,name='homepage1')









    

    


]