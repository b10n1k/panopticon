# -*- coding: utf-8 -*-
from django.shortcuts import render, get_list_or_404, redirect
from panopticon.profiles.models import UserProfile
from panopticon.diavgeia.models import Transaction
from panopticon.diavgeia.forms import TransactionForm
from panopticon.decorators import is_logged_in


def balance(transactions):
    balance = 0
    for item in transactions:
        if item.typeof == 'Income':
            balance = balance + item.amount
        else:
            balance = balance - item.amount
    return balance


@is_logged_in
def diavgeia_list(request):
    me = UserProfile.objects.get(user=request.user)
    transactions = Transaction.objects.all()[:20]
    total = balance(transactions)
    return render(request, 'diavgeia_list.html',
                  {'me': me, 'transactions': transactions, 'total': total})


@is_logged_in
def diavgeia_year(request, year):
    me = UserProfile.objects.get(user=request.user)
    transactions = get_list_or_404(Transaction.objects.filter(timestamp__year=int(year)))
    total = balance(transactions)
    return render(request, 'transactions.html',
                  {'me': me, 'transactions': transactions, 'total': total})


@is_logged_in
def diavgeia_month(request, year, month):
    me = UserProfile.objects.get(user=request.user)
    transactions = get_list_or_404(Transaction.objects.filter(timestamp__year=int(year), timestamp__month=int(month)))
    total = balance(transactions)
    return render(request, 'transactions.html',
                  {'me': me, 'transactions': transactions, 'total': total})


@is_logged_in
def diavgeia_day(request, year, month, day):
    me = UserProfile.objects.get(user=request.user)
    transactions = get_list_or_404(Transaction.objects.filter(timestamp__year=int(year), timestamp__month=int(month), timestamp__day=int(day)))
    total = balance(transactions)
    return render(request, 'transactions.html',
                  {'me': me, 'transactions': transactions, 'total': total})


@is_logged_in
def diavgeia_create(request):
    me = UserProfile.objects.get(user=request.user)
    if me.accountant:
        if request.method == 'POST':
            form = TransactionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/d/')
        else:
            form = TransactionForm()
    else:
        return redirect('/d/')
    return render(request, 'diavgeia_create.html', {'me': me, 'form': form})
