            
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from myproject.myapp.views import login
from django.contrib import admin
from myproject.myapp.views import logout_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myproject.myapp.urls')),
    url(r'^login/', login, name='login'),
    url(r'^logout_view/', logout_view, name='logout_view'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', RedirectView.as_view(url='/myapp/index/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

