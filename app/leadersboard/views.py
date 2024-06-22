from django.urls import reverse_lazy
from django.core import serializers
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.http import HttpResponse, JsonResponse

from .models import *

def user_list(request):
    if request.method == 'POST':
        UserFactory()
        return redirect('user_list')

    users = User.objects.order_by('-points').all()
    return render(request, 'user_list.html', {'list': users})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'user_detail.html', {'object': user})


def user_points_increment(request, user_id):
    user = User.objects.get(id=user_id)
    user.increment_points()
    return redirect('user_list')


def user_points_decrement(request, user_id):
    user = User.objects.get(id=user_id)
    user.decrement_points()
    return redirect('user_list')


def user_points_summary(request):
    users = User.objects.order_by('-points').all()
    users_map = {}

    for user in users:
        if not user.points in users_map:
            users_map[user.points] = {
                'names': [],
                'average_age': 0,
            }

        users_map[user.points]['names'].append(user.name)
        users_map[user.points]['average_age'] += user.age

    for key in users_map:
        users_map[key]['average_age'] = int(users_map[key]['average_age'] / len(users_map[key]['names']))

    return JsonResponse(users_map)