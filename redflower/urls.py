from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib import admin
from oscar.app import application
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.db.models import get_model
from oscar.views import handler500, handler404, handler403

from app import application

from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib.flatpages import views
from portfolio import urls, views, models



from django.conf.urls.i18n import i18n_patterns




from django.contrib import admin
admin.autodiscover()



from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap



admin.autodiscover()





urlpatterns = patterns('',

    # Examples:
        # url(r'^$', RedirectView.as_view(url='/catalogue'), name='home'),
        url(r'', include(application.urls)),


    # Robokassa integration...
    (r'^checkout/robokassa/', include('robokassa.urls')),

    url(r'^about/', include('about.urls')),

    url(r'^events/', include('events.urls')),

    url(r'^portfolio/', include('portfolio.urls')),
     url(r'^contact/', include('contact.urls')),

    url(r'^pay/', include('pay.urls')),

    url(r'^florists/', include('florists.urls')),



    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),


)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]




