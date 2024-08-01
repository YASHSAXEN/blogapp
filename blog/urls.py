from django.urls import path
from blog import views
from django.contrib import admin

urlpatterns = [
    path('',views.Home,name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('blogs/',views.Blogs,name='blogs'),
    path('blogdetail/<int:id>',views.Blogdetail,name='blogdetail'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.LogIn,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('changepass/',views.ChangePassword,name='changepass'),
    path('forgotpass/<int:userid>/<slug:otp>/',views.ForgotPassword,name='forgotpass'),
    path('dashboard/',views.DashBoard,name='dashboard'),
    path('deleteblog/<int:id>',views.DeleteBlog,name='deleteblog'),
    path('editblog/<int:id>',views.EditBlog,name='editblog'),
    path('addblog/',views.AddBlog,name='addblog'),
    path('profile/',views.Profile,name='profile'),
    path('contactus/',views.Contactus,name='contactus')
]