#definde our url patten and map it to our api methode

from django.urls import re_path
from EmployeeApp import views

from django.conf.urls.static import static
#static path so that we can access media file via url that is 
from django.conf import settings
# use for media til

urlpatterns = [
    re_path(r'^department/$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),
    # if url start with "department", we need to map it to 
    # department api method and if if url start with "department" +
    #id you still map it to department
    re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)