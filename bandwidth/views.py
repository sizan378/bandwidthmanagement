from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import *


def index(request):
    if request.user.is_authenticated:
        post = article.objects.all()
        posts = upgrade.objects.all()
        search = request.GET.get('q')
        if search:
            post=post.filter(
                Q(pop_name__icontains=search)
            )
        paginator = Paginator(post, 50) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "post":page_obj,
            'posts':posts
        
        }
        return render(request, "index.html", context)
    else:
        return redirect('login')
    

def getauthor(request, name):
    post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=post_author)
    post = article.objects.filter(article_author=auth.id)
    return render(request, "profile.html", {'post':post, 'auth':auth})

def getTopic(request, name):
    cat = get_object_or_404(category, name=name)
    post = article.objects.filter(category=cat.id)
    return render(request, "category.html",{'post':post, 'cat':cat})

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            user = request.POST.get('username')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('profile')
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect('login')

def getUpgrade(request):
    return render(request,'upgrade.html')

def getDowngrade(request):
    form = downgradeForm(request.POST or None)
    u=get_object_or_404(author, name=request.user.id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.article_author=u
        instance.save()
        return redirect('profile')
    return render(request,'downgrade.html',{'form':form})


def getRequest(request):
    post = article.objects.all()
    context = {
        "post":post,
       
    }
    return render(request, 'request.html',context)

def getProfile(request):
    if request.user.is_authenticated:
        post = article.objects.filter(article_author=request.user.id)
        # post = article.objects.all()
        posts = upgrade.objects.filter(upgrade_author=request.user.id)

        return render(request,'login_profile.html',{'post':post, 'posts':posts})

    else:
        return redirect('login')


def getUpdate(request,id):
    if request.user.is_authenticated:
        # u=get_object_or_404(author, name=request.user.id)
        post= get_object_or_404(article, pk=id)
        updated = upgrade.objects.filter(post=id)
        form = UpdateForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.article_author = u
            instance.post=post
            instance.save()
            return redirect('profile')
        context ={
            'form':form, 
            'post':post,
            'updated':updated
            }
        return render(request, 'update.html',context)
    else:
        return redirect( 'login')