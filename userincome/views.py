from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from .models import UserIncome, Source
from userpreferences.models import UserPreferences


@login_required(login_url='authentication/login')
def index(request):
    sources = Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)
    paginator = Paginator(income, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreferences.objects.get(user=request.user).currency
    context = {'income': income,
               'page_obj': page_obj,
               'currency': currency}
    return render(request, 'income/index.html', context=context)


@login_required(login_url='authentication/login')
def add_income(request):
    sources = Source.objects.all()
    context = {'sources': sources,
               'values': request.POST}
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context=context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        source = request.POST['source']
        date = request.POST['income_date']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'income/add_income.html', context=context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'income/add_income.html', context=context)

        UserIncome.objects.create(owner=request.user, amount=amount, description=description, date=date, source=source)
        messages.success(request, 'Record saved successfully')
        return redirect('income')

