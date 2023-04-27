from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import AuthenticationForm
from .models import Post, Topic, Comment
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


@login_required(login_url='/login/')
def main(request):
    search_params = Q()
    if request.GET.get('search_req'):
        search_params |= Q(title__icontains=request.GET.get('search_req'))
    if request.GET.get('topic'):
        search_params |= Q(contains__title__icontains=request.GET.get('topic'))
    posts = Post.objects.filter(search_params)
    topics = Topic.objects.all()
    return render(request, 'blogs.html', {'data': posts,
                                          'topics': topics})


def about(request):
    return HttpResponse('This is ABAAAAAAAAAAAAAAAAAUTTT')


@login_required(login_url='/login/')
def blog_post(request, slug):
    if request.GET.get('comment_text'):
        Comment.objects.create(content=request.GET.get('comment_text'),
                               contains=Post.objects.get(slug=slug),
                               author=User.objects.get(username=request.user))

    post = Post.objects.get(slug=slug)
    comments = post.comment_set.all()
    return render(request, 'blog_item.html', {"data": post, "comments": comments})


def blog_post_add_comment(request, slug):
    return HttpResponse(f'This is page for adding comment to post №{slug}')


@login_required(login_url='/login/')
def create_new_post(request):
    if request.method == 'POST':
        new_post = Post(title=request.POST.get('title'),
                        text=request.POST.get('post_body'),
                        author=User.objects.get(username=request.user))
        topics_lst = request.POST.getlist('topics')
        new_post.save()
        for topic in topics_lst:
            new_post.contains.add(Topic.objects.get(title=topic))

    topics = Topic.objects.all()
    return render(request, 'created_post.html', {'topics': topics})


def update_post(request, slug):
    return HttpResponse(f'This is update form for post {slug}')


def delete_post(request, slug):
    return HttpResponse(f'NOOOOOOO!'
                        f'GOD!!!'
                        f'Please NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!'
                        f'Don\'t delete post {slug}')


def show_user_profile(request, username):
    return HttpResponse(f'This is property of the {username}')


def change_password(request, username):
    return HttpResponse(f'Hey {username}. Tell me your password, Bro :)')


def register_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('name'),
                                        password=request.POST.get('password'),
                                        first_name=request.POST.get('first_name'),
                                        last_name=request.POST.get('second_name'))
        user.save()
    return render(request, 'registretion.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
