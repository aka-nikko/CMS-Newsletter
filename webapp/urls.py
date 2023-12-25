from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView, name="home"),
    path('register/',views.registerView, name="register"),
    path('login/',views.loginView, name="login"),
    path('addtopic/',views.addtopicView, name="addtopic"),
    path('newsubmission/',views.newsubmissionView, name="newsubmission"),
    path('submissions/',views.submissionsView, name="submissions"),
    path('submission/<str:pk>/',views.submissionView, name="submission"),
    path('submission/<str:pk>/update/',views.submissionupdateView, name="submissionupdate"),
    path('publish/',views.publishView, name="publish"),
    path('editsubmissions/', views.editsubmissionsView, name='editsubmissions'),
    path('newsletters/',views.newslettersView, name="newsletters"),
    path('newsletter/<str:pk>/',views.newsletterView, name="newsletter"),
    path('newsletter/<str:pk>/update/',views.newsletterupdateView, name="newsletterupdate"),
    path('newsletter/<str:pk>/download/', views.docxView, name='docxdownload'),
    path('search/', views.searchView, name='search'),
    path('logout/',views.logoutView, name="logout"),
]