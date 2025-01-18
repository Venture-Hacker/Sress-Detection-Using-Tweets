from django.urls import path
from.import views
from django.contrib.auth.views import LoginView

urlpatterns=[

    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('afterlogin',views.afterlogin_view,name="afterlogin"),
    path('logout/', views.logout_user, name="logout"),
    path('home/',views.home,name="home"),
    path('predict/',views.predict,name="predict"),
    path('profile/',views.profile,name="profile"),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('consult/',views.consult,name="consult"),
    path('consult1/',views.consult1,name="consult1"),



]
