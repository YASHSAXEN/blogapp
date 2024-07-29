from django.shortcuts import render, redirect
from blog.models import Blog, ContactUs
from datetime import datetime
from django.contrib import messages
from blog.forms import SignUpForm, LoggedInForm, ChangePassForm, EditBlogForm, UserProfileForm, ContactUsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import hashlib
import random

def is_loggedin(request):
    status = request.user.is_authenticated
    if status:
        show = request.user.username[0].upper()
    else:
        show = None  
    return status,show

def Home(request):
    status,show = is_loggedin(request)  
    return render(request,'blog/home.html',{'show':show,'status':status})

def Blogs(request):
    status,show = is_loggedin(request) 
    blogs = Blog.objects.all()
    return render(request,'blog/blogs.html',{"blogs":blogs,'show':show,'status':status})

def Blogdetail(request,id):
    status,show = is_loggedin(request) 
    blog_detail = Blog.objects.get(id=id)
    comments = eval(blog_detail.comments)
    if request.method == 'POST':
        comment_by = request.user.username
        comment_content = request.POST['comment_content']
        comment_at = str(datetime.now()).split(".")[0]
        comment_details = [comment_by,comment_content,comment_at]
        comments.append(comment_details)
        blog_detail.comments = str(comments)
        blog_detail.comments_count = len(comments)
        blog_detail.save()
        if request.user.username != blog_detail.author:
            email = User.objects.filter(username=blog_detail.author)[0].email
            subject = "Blog App: Someone comment on your post"
            message = f"User: {request.user.username} comment on your blog.\nBlog: {blog_detail.title}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,from_email,recipient_list)
    return render(request,'blog/blog_detail.html',{'blogdetail':blog_detail,'show':show,'status':status,"comments":comments})

def Signup(request):
    if not request.user.is_authenticated:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'SignedUp Successfully!!')
                form = SignUpForm()
        return render(request,'blog/signup.html',{'form':form})
    else:
        return redirect('/dashboard/')

def LogIn(request):
    if not request.user.is_authenticated:
        form = LoggedInForm(request=request)
        if request.method == 'POST':
            form = LoggedInForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                userobj = authenticate(username=username,password=password)
                if userobj:
                    login(request,userobj)
                    return redirect('/dashboard/')
        return render(request,'blog/login.html',{'form':form})
    else:
        return redirect('/dashboard/')

def Logout(request):
    logout(request)
    return redirect('/')

def ChangePassword(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
            username = request.POST['username']
            userobj = User.objects.filter(username=username)
            if userobj:
                otp = str(random.randint(1000,10000))
                hased_otp = hashlib.sha256(otp.encode()).hexdigest()
                userid = userobj[0].id
                email = userobj[0].email
                subject = "This mail regarding the change of your Blog app password"
                message = f"The otp for changing your django app password {otp}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject,message,from_email,recipient_list)
                messages.success(request,f"Please enter otp send on {email}")
                return redirect(f'/forgotpass/{userid}/{hased_otp}')
            else:
                messages.warning(request,"😡😡 Please Enter Valid Username 😡😡")
        return render(request,'blog/changepass.html')
    else:
        return redirect('/dashboard/')
    
def ForgotPassword(request,userid,otp):
    if not request.user.is_authenticated: 
        userobj = User.objects.get(id=userid)
        form = ChangePassForm(user=userobj)
        if request.method == 'POST':
            form = ChangePassForm(user=userobj,data=request.POST)
            if form.is_valid():
                otp_entered = form.cleaned_data.get('otp',0)
                hased_otp_entered = hashlib.sha256(str(otp_entered).encode()).hexdigest()
                if hased_otp_entered == otp:
                    form.save()
                    return redirect('/login/')
                else:
                    messages.error(request,"😡😡The otp is invalid. Please enter the valid email.😡😡")
        return render(request,'blog/forgotpass.html',{'form':form})
    else:
        return redirect('/')

def DashBoard(request):
    if request.user.is_authenticated: 
        status,show = is_loggedin(request)
        userdetails = request.user
        userblogs = Blog.objects.filter(author=request.user.username)
        return render(request,'blog/dashboard.html',{'show':show,'status':status,"userdetails":userdetails,"blogs":userblogs})
    else:
        return redirect('/login/')

def DeleteBlog(request,id):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id = id)
        blog.delete()
        return redirect('/dashboard/')
    else:
        return redirect('/login/')

def EditBlog(request,id):
    if request.user.is_authenticated:
        status,show = is_loggedin(request) 
        blog = Blog.objects.get(id = id)
        form = EditBlogForm(initial={'title':blog.title,"content":blog.content})
        if request.method == 'POST':
            form = EditBlogForm(request.POST)
            if form.is_valid():
                blog.title = form.cleaned_data['title']
                blog.content = form.cleaned_data['content']
                blog.updated_at = datetime.now()
                blog.is_updated = True
                blog.save()
                return redirect('/dashboard/')
        return render(request,'blog/editblog.html',{"blog":blog,'form':form,'show':show,'status':status})
    else:
        return redirect('/login/')
    
def AddBlog(request):
    if request.user.is_authenticated:
        status,show = is_loggedin(request) 
        form = EditBlogForm()
        if request.method == 'POST':
            print('yes')
            form = EditBlogForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                print(title)
                print(content)
                blog = Blog(title=title, content=content, created_at=datetime.now(),comments="[]",author=request.user.username,updated_at=datetime.now())
                blog.save()
                return redirect('/dashboard/')
        return render(request,'blog/addblog.html',{'form':form,'show':show,'status':status})
    else:
        return redirect('/login/')
    
def Profile(request):
    if request.user.is_authenticated:
        status,show = is_loggedin(request) 
        username = request.user.username
        last_login = request.user.last_login
        date_joined = request.user.date_joined
        form = UserProfileForm(instance = request.user)
        if request.method == 'POST':
            form = UserProfileForm(instance = request.user, data=request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                user = User.objects.get(id=request.user.id)
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.last_login = last_login
                user.date_joined = date_joined
                user.email = email
                user.save()
                messages.success(request,'Profile has been updated Successfully!!')
                return redirect('/dashboard/')
        return render(request,'blog/profile.html',{'show':show,'status':status,'form':form})
    else:
        return redirect('/login/')
    
def Contactus(request):
    status,show = is_loggedin(request)
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            contact = ContactUs(username=request.user.username,title=title,description=description,created_at=datetime.now())
            contact.save()
            form = ContactUsForm()
            messages.success(request,'Your query has been successfully submiitted. Our team will reach out you soon!!')
    return render(request,'blog/contactus.html',{'show':show,'status':status,'form':form})