from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    return render(request, 'blogs.html')


def about(request):
    return HttpResponse('This is ABAAAAAAAAAAAAAAAAAUTTT')


def blog_post(request, slug):
    return render(request, 'blog_item.html')


def blog_post_add_comment(request, slug):
    return HttpResponse(f'This is page for adding comment to post №{slug}')


def create_new_post(request):
    return HttpResponse('Thi is form for create new post')


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
    return render(request, 'registretion.html')


def login_user(request):
    return render(request, 'login.html')
