from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'experts'
urlpatterns = [
    path('',views.home, name='home'),
    path('news',views.news,name='news'),
    path('expert/<int:expert_id>',views.expert,name='expert'),
    path('topic/<int:topic_id>',views.topic,name='topic'),
    path('search',views.search,name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)