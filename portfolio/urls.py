from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^/$', 'portfolio.views.home', name=home),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'brochure.views.home', name='home'),
    url(r'^blog/(?P<blog_id>\w+)/$', 'brochure.views.blog', name='blog'),
    url(r'^contact/$', 'brochure.views.contact', name='contact'),



)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
