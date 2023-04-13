from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import Expert, Topic, News

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        expertsearched = Expert.objects.filter(expert_Name__contains=searched)
        topicsearched = Topic.objects.filter(topic_Name__contains=searched)
        return render(request,'experts/search.html',{'searched':searched,
                                                     'expertsearched':expertsearched,
                                                     'topicsearched':topicsearched})
    else:
        return render(request,'experts/search.html',{})



def home(request):
    experts_list = Expert.objects.order_by('-expert_Name')
    topics_list = Topic.objects.order_by('-topic_Name')
    context = {'experts_list' : experts_list,'topics_list' : topics_list}
    return render(request,'experts/home.html',context)

def expert(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    return render(request, 'experts/expert.html',{'expert':expert})

def topic(request, topic_id):
    experts_list = Expert.objects.order_by('-expert_Name')
    topic_object = get_object_or_404(Topic, pk=topic_id)
    context = {'experts_list' : experts_list,'topic_object' : topic_object}
    return render(request, 'experts/topic.html',context)

def news(request):
    experts_list = Expert.objects.order_by('-expert_Name')
    topics_list = Topic.objects.order_by('-topic_Name')
    news_list = News.objects.order_by('-created_at')
    context = {'experts_list' : experts_list,'topics_list' : topics_list,'news_list':news_list}
    return render(request, 'experts/news.html',context)