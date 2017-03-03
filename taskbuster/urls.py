from django.conf.urls import include, url
from django.contrib import admin
from .views import home, home_files
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', home, name='home'),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

]
# <span class="crayon-v">urlpatterns</span> <span class="crayon-o">+=</span> <span class="crayon-e">i18n_patterns</span><span class="crayon-sy">(
#    ...
# )</span>

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
