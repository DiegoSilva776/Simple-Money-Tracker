from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from expenses import views

# Allow passing the content type at the end of the Request url and name all endpoints but the root
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^expenses/$', views.ExpenseList.as_view(), name='expense-list'),
    url(r'^expenses/(?P<pk>[0-9]+)/$', views.ExpenseDetail.as_view(), name='expense-detail'),
    url(r'^expenses/(?P<pk>[0-9]+)/highlight/$', views.ExpenseHighlight.as_view(), name='expense-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])

# Add the default login and logout endpoints from the DjangoREST framework to the app
# The r'^api-auth/' part of pattern can actually be whatever URL you want to use. 
# The only restriction is that the included urls must use the 'rest_framework' namespace.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
