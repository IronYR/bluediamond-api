from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include blog app's URLs
    # path('index/',TemplateView.as_view(template_name='index.html') ),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
    # re_path(r'^(?!static/.*|assets/.*|api/.*|admin/.*$).*', TemplateView.as_view(template_name='index.html')),

]
# if settings.DEBUG:
#     # This is to serve static files in development
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)