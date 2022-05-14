from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .permissions import HasRestaurantPermissionsOrReadOnly
from menus_project.constants import FRONTEND_SERVER_URL_CONFIRM_EMAIL
from restaurants.models import Restaurant
from menus.models import Menu, MenuSection, MenuItem

UserModel = get_user_model()
from django.shortcuts import render

# Create your views here.
