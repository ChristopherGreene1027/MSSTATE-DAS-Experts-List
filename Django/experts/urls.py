from django.urls import path

from . import views

app_name = 'experts'
urlpatterns = [
    path('',views.home, name='home'),
    path('news',views.news,name='news'),
    path('expert/<int:expert_id>',views.expert,name='expert'),
    path('topic/<int:topic_id>',views.topic,name='topic'),
]