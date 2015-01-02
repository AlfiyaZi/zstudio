__author__ = 'alya'

#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from contact.models import Contact

from contact.forms import ContactForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import redirect

import smsru






def index(request):
    context = RequestContext(request)

    return render_to_response('contact/index.html',  context)


def add_contact(request):
    # Get the context from the request.
    context = RequestContext(request)


    context_dict = {}


    # A HTTP POST?
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            print form.cleaned_data
            mes=form.data['name']+form.data['phone']+ form.data['message']
            umes=unicode(mes)


            form.save(commit=True)


            import smsru
            cli = smsru.Client()
            cli.send("+79526646699", umes )



            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
	        # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ContactForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    context_dict['form'] = form
    return render_to_response('contact/add_contact.html', context_dict, context)

