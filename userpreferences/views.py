from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
import json
import os
import pdb
from .models import UserPreferences


def index(request):
    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    with open(file_path, 'r') as josn_file:
        data = json.load(josn_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = UserPreferences.objects.filter(user=request.user).exists()
    user_preferences = None

    if exists:
        user_preferences = UserPreferences.objects.get(user=request.user)

    if request.method == 'GET':
        return render(request, 'preferences/index.html', context={'currencies': currency_data, 'user_preferences': user_preferences})

    else:
        currency = request.POST['currency']
        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreferences.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changes saved')
        return render(request, 'preferences/index.html', context={'currencies': currency_data, 'user_preferences': user_preferences})

