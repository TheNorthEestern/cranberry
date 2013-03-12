# from trelloclone.api import BoardResource, CardResource, UserResource
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from rest_framework.urlpatterns import format_suffix_patterns
import views
from .decorators import anonymous_required

urlpatterns = patterns('',
    url(r'^$', login_required(direct_to_template), {'template':'index/index.html'} ),
    url(r'accounts/login/$', anonymous_required(login)),
    url(r'api/v1/$', views.api_root),
    url(r'api/v1/boards/$', views.BoardList.as_view(), name='board-list'),
    url(r'api/v1/boards/(?P<pk>[0-9]+)/$', views.BoardDetail.as_view(), name='board-detail'),
    url(r'api/v1/boards/(?P<pk>[0-9]+)/cards/$', views.card_relative_to_parent_detail),
    url(r'api/v1/cards/$', views.CardList.as_view(), name='card-list'),
    url(r'api/v1/cards/(?P<pk>[0-9]+)/$', views.CardDetail.as_view(),name='card-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', anonymous_required(login)),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
)
