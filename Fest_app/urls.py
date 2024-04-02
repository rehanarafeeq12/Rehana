from django.urls import path

from Fest_app import admin_views, user_views, views


urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('yearloginpage',views.yearloginpage,name='yearloginpage'),
    path('registerpage',views.registerpage,name='registerpage'),
    path('adminpage',admin_views.adminpage,name='adminpage'),
    path('schoolregister',views.schoolregister,name='schoolregister'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('main_admin',views.main_admin,name='main_admin'),
    path('school_view',views.school_view,name='school_view'),
    path('approve_school/<int:id>/',views.approve_school,name='approve_school'),
    path('student_view',views.student_view,name='student_view'),
    path('contestadd',admin_views.contestadd,name='contestadd'),
    path('contestview',admin_views.contestview,name='contestview'),
    path('update_list/<int:id>/',admin_views.update_list,name='update_list'),
    path('del_list/<int:id>/',admin_views.del_list,name='del_list'),
    path('participant_add',admin_views.participant_add,name='participant_add'),
    path('participant_view',admin_views.participant_view,name='participant_view'),
    path('update_participant/<int:id>/',admin_views.update_participant,name='update_participant'),
    path('del_participant/<int:id>/',admin_views.del_participant,name='del_participant'),
    path('judges_add',admin_views.judges_add,name='judges_add'),
    path('judges_view',admin_views.judges_view,name='judges_view'),
    path('update_judges/<int:id>/',admin_views.update_judges,name='update_judges'),
    path('del_judges/<int:id>/',admin_views.del_judges,name='del_judges'),
    path('result_add',admin_views.result_add,name='result_add'),
    path('result_view',admin_views.result_view,name='result_view'),
    path('update_result/<int:id>/',admin_views.update_result,name='update_result'),
    path('del_result/<int:id>/',admin_views.del_result,name='del_result'),
    path('programmes_add',admin_views.programmes_add,name='programmes_add'),
    path('programmes_view',admin_views.programmes_view,name='programmes_view'),
    path('update_programmes/<int:id>/',admin_views.update_programmes,name='update_programmes'),
    path('del_programmes/<int:id>/',admin_views.del_programmes,name='del_programmes'),
    path('performer_add',admin_views.performer_add,name='performer_add'),
    path('performer_view',admin_views.performer_view,name='performer_view'),
    path('update_performer/<int:id>/',admin_views.update_performer,name='update_performer'),
    path('del_performer/<int:id>/',admin_views.del_performer,name='del_performer'),
    path('venue_add',admin_views.venue_add,name='venue_add'),
    path('venue_view',admin_views.venue_view,name='venue_view'),
    path('update_venue/<int:id>/',admin_views.update_venue,name='update_venue'),
    path('del_venue/<int:id>/',admin_views.del_venue,name='del_venue'),
    path('volunteers_add',admin_views.volunteers_add,name='volunteers_add'),
    path('volunteers_view',admin_views.volunteers_view,name='volunteers_view'),
    path('update_volunteers/<int:id>/',admin_views.update_volunteers,name='update_volunteers'),
    path('del_volunteers/<int:id>/',admin_views.del_volunteers,name='del_volunteers'),
    path('guests_add',admin_views.guests_add,name='guests_add'),
    path('guests_view',admin_views.guests_view,name='guests_view'),
    path('update_guests/<int:id>/',admin_views.update_guests,name='update_guests'),
    path('del_guests/<int:id>/',admin_views.del_guests,name='del_guests'),
    path('gallery_add',admin_views.gallery_add,name='gallery_add'),
    path('gallery_view',admin_views.gallery_view,name='gallery_view'),
    path('update_gallery/<int:id>/',admin_views.update_gallery,name='update_gallery'),
    path('del_gallery/<int:id>/',admin_views.del_gallery,name='del_gallery'),
    path('achievements_add',admin_views.achievements_add,name='achievements_add'),
    path('achievements_view',admin_views.achievements_view,name='achievements_view'),
    path('update_achievements/<int:id>/',admin_views.update_achievements,name='update_achievements'),
    path('del_achievements/<int:id>/',admin_views.del_achievements,name='del_achievements'),
    path('management_add',admin_views.management_add,name='management_add'),
    path('management_view',admin_views.management_view,name='management_view'),
    path('update_management/<int:id>/',admin_views.update_management,name='update_management'),
    path('del_management/<int:id>/',admin_views.del_management,name='del_management'),
    path('teachers_add',admin_views.teachers_add,name='teachers_add'),
    path('teachers_view',admin_views.teachers_view,name='teachers_view'),
    path('update_teachers/<int:id>/',admin_views.update_teachers,name='update_teachers'),
    path('del_teachers/<int:id>/',admin_views.del_teachers,name='del_teachers'),
    path('history_add',admin_views.history_add,name='history_add'),
    path('history_view',admin_views.history_view,name='history_view'),
    path('update_history/<int:id>/',admin_views.update_history,name='update_history'),
    path('del_history/<int:id>/',admin_views.del_history,name='del_history'),
    

    path('contestlist',user_views.contestlist,name='contestlist'),
    path('participantlist',user_views.participantlist,name='participantlist'),
    path('judgeslist',user_views.judgeslist,name='judgeslist'),
    path('resultlist',user_views.resultlist,name='resultlist'),
    path('guestlist',user_views.guestlist,name='guestlist'),
    path('programlist',user_views.programlist,name='programlist'),
    path('venue_vol',user_views.venue_vol,name='venue_vol'),
    path('photoshop',user_views.photoshop,name='photoshop'),
    path('school_achievements',user_views.school_achievements,name='school_achievements'),
    path('tchrs',user_views.tchrs,name='tchrs'),
    path('mngmnt',user_views.mngmnt,name='mngmnt'),
    path('feedbacks_add',user_views.feedbacks_add,name='feedbacks_add'),
    path('feedbacks_view',user_views.feedbacks_view,name='feedbacks_view'),
    path('aboutpage',user_views.aboutpage,name='aboutpage'),
    path('contactpage',user_views.contactpage,name='contactpage'),
    path('supportpage',user_views.supportpage,name='supportpage'),
    path('success',user_views.success,name='success'),
    path('year_add',admin_views.year_add,name='year_add'),
    path('admin1page',admin_views.admin1page,name='admin1page'),
    path('year_view',admin_views.year_view,name='year_view'),
    path('school_history',user_views.school_history,name='school_history'),
    path('homepage',views.homepage,name='homepage'),
    path('logout', views.logout, name='logout'),
    path('explorepage',user_views.explorepage,name='explorepage')









    

    


]