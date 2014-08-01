from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'supernode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'authen.views.user_registration'),
    url(r'^checkvalidemail','authen.views.checkValidEmail'),
    url(r'^logincheck','authen.views.logincheck')
)
