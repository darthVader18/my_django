from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")


def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'app_two/help.html', context=helpdict)


def index(request):
    return render(request, 'app_two/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users": user_list}
    return render(request, 'app_two/users.html', context=user_dict)
