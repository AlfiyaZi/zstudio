#!/usr/bin/env python2.6
import os
import sys
import site
import urllib 
# Tell Passenger to run our virtualenv python
INTERP = "/home/xnabcfag/djangoenv/bin/python"
print INTERP
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
# Setup paths and environment variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'redflower.settings'
# Set the application
import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
# Use paste to display errors
application = ErrorMiddleware(application, debug=True)

class PassengerPathInfoFix(object):
    """
    Sets PATH_INFO from REQUEST_URI since Passenger doesn't provide it.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        from urllib import unquote
        request_uri = unquote(environ['REQUEST_URI'])
        script_name = unquote(environ.get('SCRIPT_NAME', ''))
        offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
        environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
        return self.app(environ, start_response)


application = PassengerPathInfoFix(application)