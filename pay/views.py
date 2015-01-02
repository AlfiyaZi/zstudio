#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from robokassa.forms import *


@login_required
def pay(request):
   # order = get_object_or_404(Order, pk=order_id)

    form = RobokassaForm(initial={
               #'orderId': 7,
               'OutSum': Decimal('10.00'),
               'InvId': 58,
               'Desc' : u'Холодильник "Бирюса"',
               'Email': request.user.email,
                #'IncCurrLabel': '',
                #'Culture': 'ru'
           })

    return render(request, 'pay/pay.html', {'form': form})




def pay1(request):
    if request.method == 'POST': # If the form has been submitted...

        form = RobokassaForm(request.POST) # A form bound to the POST data
        if form.is_valid():
              form.save(commit=True)


    else:
        form = RobokassaForm() # An unbound form

    return render(request, 'pay/pay1.html', {
        'form': form,
    })


