from django.core.mail import send_mail
from testApp.forms import Mail_Send_Form
from testApp.forms import Comment_Form
from django.shortcuts import render, get_object_or_404, redirect
from testApp.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from django.db.models import Count,Q
from django.contrib.auth.decorators import login_required
from testApp.forms import Signup_Form,Recipe_Form
from django.http import HttpResponse
import json
import requests

# Create your views here.

def home_view(request):
    return render(request,'testApp/home.html')

def about_view(request):
    return render(request,'testApp/about.html')

def contact_view(request):
    return render(request,'testApp/contact.html')

def post_list_view(request, tag_slug=None):
    post_list = Post.objects.all().order_by('-publish')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'testApp/post_list.html', {'post_list': post_list, 'tag': tag})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    post_tags = post.tags.all()
    similar_post = Post.objects.filter(status = 'published',tags__in=post_tags)
    similar_post = similar_post.annotate(tag_count=Count('tags')).order_by('-tag_count','-created')

    comments = post.comments.filter(active=True)
    csubmit = False

    if request.method == 'POST':
        form = Comment_Form(request.POST,request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True

    else:
        form = Comment_Form()

    return render(request, 'testApp/post_detail.html', {'post': post, 'form': form, 'csubmit': csubmit, 'comments': comments,'similar_post':similar_post})


def mail_send_view(request, id):

    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    form = Mail_Send_Form()
    if request.method == 'POST':
        form = Mail_Send_Form(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            subject = '{} ({}) Recommends you to Read {} Post'.format(
                cleaned_data['name'], cleaned_data['email'], post.title)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = 'Read Post At: \n\n {}\n\n{}\'s Comments:\n\n{}'.format(
                post_url, cleaned_data['name'], cleaned_data['comments'])
            send_mail(subject, message, 'shubham.wankar@gmail.com',
                      [cleaned_data['to']])
            sent = True
    return render(request, 'testApp/sendmail.html', {'form': form, 'post': post, 'sent': sent})

def breakfast_view(request, tag_slug=None):
    post_list = Post.objects.all().filter(category='Breakfast')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'testApp/category.html', {'post_list': post_list, 'tag': tag})

def lunch_view(request, tag_slug=None):
    post_list = Post.objects.all().filter(category='Lunch')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'testApp/category.html', {'post_list': post_list, 'tag': tag})

def dinner_view(request, tag_slug=None):
    post_list = Post.objects.all().filter(category='Dinner')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'testApp/category.html', {'post_list': post_list, 'tag': tag})

def dessert_view(request, tag_slug=None):
    post_list = Post.objects.all().filter(category='Desserts')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'testApp/category.html', {'post_list': post_list, 'tag': tag})

def add_view(request):
    return render(request,'testApp/post_list.html')

def signup_view(request):
    form = Signup_Form()
    if request.method=='POST':
        form = Signup_Form(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')

    return render(request,'testApp/signup.html',{'form':form})

def logout_view(request):
    return render(request,'testApp/logout.html')

def add_view(request):
    form = Recipe_Form()
    if request.method=='POST':
        form = Recipe_Form(request.POST,request.FILES)
        form.save()

        return redirect('/')

    return render(request,'testApp/recipe.html',{'form':form})

def search_view(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        post_list = Post.objects.filter(title__icontains=searched) | Post.objects.filter(user_detail__icontains=searched) | Post.objects.filter(category__icontains=searched)
        return render(request,'testApp/search.html',{'post_list':post_list,'searched':searched})
    else:
        return render(request,'testApp/search.html',{})
    
def api_signup(request):
    form = Signup_Form()
    if request.method=='POST':
        form = Signup_Form(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/api/auth-jwt/')
    return render(request,'testApp/signup.html',{'form':form})
