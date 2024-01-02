# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'myproject.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]
# myproject/urls.py
from django.conf.urls import url, include
from dashboard.views import dashboard_view

urlpatterns = [
    url(r'^dashboard/$', dashboard_view, name='dashboard_view'),
    # Add other URL patterns as needed
]
