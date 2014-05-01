from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'signapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^result/', 'tennis.views.result', name='result'),
    #url(r'^templates/', 'signapps.views.start', name='mian'),
    #url(r'^$', 'django.views.generic.simple.direct_to_template', { 'template': 'mian.html' }),
    url(r'^$', TemplateView.as_view(template_name='mian.html'), name="home"),
    url(r'^players$', TemplateView.as_view(template_name='players.html'), name="home"),
    url(r'^tournaments$', TemplateView.as_view(template_name='tournaments.html'), name="home"),
    url(r'^ranking$', TemplateView.as_view(template_name='ranking.html'), name="home"),
    
    url(r'^page1$', 'signapps.views.players', name='players'),
    url(r'^h2h$', 'signapps.views.h2h', name='h2h'),
    url(r'^searchResult$', 'signapps.views.searchResult', name='Search Results'),
    url(r'^recentResult$', 'signapps.views.recentResult', name='Recent Results'),
    url(r'^individualRank$', 'signapps.views.individualRank', name='Individual Rank'),
    url(r'^playerByRank$', 'signapps.views.playerByRank', name='Player By Rank'),
    url(r'^completeRanking$', 'signapps.views.completeRanking', name='Complete Ranking'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
