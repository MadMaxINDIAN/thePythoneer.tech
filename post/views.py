from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import BlogPost
from django.contrib import messages
from json import dumps
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, FeedbackForm, CreateUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(req):
    blogs = BlogPost.objects.all()
    data = {
        'title': "Home",
        'blog': "thePythoneer.tech",
        'blogs': blogs
    }
    return render(req, 'home.html', data)

def comment(req, blog_title):
    if req.method == 'POST':
        blog = BlogPost.objects.filter(title=blog_title)[0]
        
        return
    return HttpResponse("This is the wrong url.")


# # # # # # # # # # # # # # # # # # # # #    BLOG SECTION    # # # # # # # # # # # # # # # # # # # # # 
# api => "/b/<str:blog_title>"
# request => GET, POST
# returns => blog post with title = blog_title
def blog(req,blog_title):
    blog = BlogPost.objects.filter(title=blog_title)[0]
    tags = blog.tags.all()
    feedback_form = FeedbackForm(instance=blog)
    if req.method == 'POST':
        
        blog = BlogPost.objects.filter(title=blog_title)[0]
        blog.feedback_amazed += int(req.POST['feedback_amazed'])
        blog.feedback_loved += int(req.POST["feedback_loved"])
        blog.feedback_upvote += int(req.POST['feedback_upvote'])
        blog.save()
        res = {
            'feedback_amazed': blog.feedback_amazed,
            'feedback_loved': blog.feedback_loved,
            'feedback_upvote': blog.feedback_upvote,
        }
        return JsonResponse(res)
    return render(req, 'blog.html',{'title': blog.title,'blog': "thePythonner.tech",'post': blog,'tags': tags, 'feedback_form': feedback_form})

@login_required(login_url="/u/login_user")
def create_blog(req):
    form = BlogPostForm()
    context = {
        'form': form
    }
    if req.method == 'POST':
        form = BlogPostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(req, 'create_blog.html',{'title': "Create Blog Post",'blog': "thePythonner.tech", 'form': form})

@login_required(login_url="/")
def update_blog(req, title):
    blog = BlogPost.objects.filter(title=title)[0]
    form = BlogPostForm(instance=blog)
    context = {
        'form': form
    }
    if req.method == 'POST':
        form = BlogPostForm(req.POST, req.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(req, 'create_blog.html',{'title': "Create Blog Post",'blog': "thePythonner.tech", 'form': form})


# # # # # # # # # # # # # # # # # # # # #    USER SECTION    # # # # # # # # # # # # # # # # # # # # # 
def create_user(req):
    print(req.POST.get('next',""))
    if req.user.is_authenticated:
        return redirect("/")
    errors = {}
    form = CreateUser()
    if req.method == "POST":
        form = CreateUser(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, "Account has been created for " + user)
            return redirect("/u/login_user")
        else:
            for key in form.errors:
                errors[key] = form.errors[key][0]
            print(errors)
    data = {
        'form': form,
        'errors': errors,
        'data': req.POST
    }
    return render(req,"register_user.html",data)


def login_user(req):
    if req.user.is_authenticated:
        return redirect("/")
    data = {}
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect("/")
        else:
            messages.info(req, "Username or Password is incorrect")
    return render(req,"login_user.html",data)

def logout_user(req):
    logout(req)
    return redirect("/u/login_user")