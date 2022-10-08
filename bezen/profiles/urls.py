from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('register', views.UserRegister.as_view(), name="register"),
               path('profilecreate',views.CreateProfile.as_view(),name="profilecreate"),
               path('home',views.UserHome.as_view(),name="userhome"),
               path('login',views.SignIn.as_view(),name="login"),
               path('logout',views.SignOut.as_view(),name="logout"),
               path('profileview',views.ViewProfile.as_view(),name="profileview"),
               path('profileedit',views.EditProfile.as_view(),name="profileedit"),
]