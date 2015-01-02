#!/usr/bin/python
# -*- coding: utf-8 -*-


from django import forms
from django.contrib.auth.models import User
from contact.models import Contact
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text=u"Ваше имя")
    phone = forms.CharField(max_length=15, help_text=u"Номер телефона")
    message = forms.CharField(widget=forms.Textarea(attrs={ 'rows': 3}), max_length=250, help_text=u" Дополнительная информация")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Contact