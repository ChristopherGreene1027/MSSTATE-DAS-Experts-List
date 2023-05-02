from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import Expert, Topic, News
from django.core.paginator import Paginator

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
    #expertImg = Expert.objects.expert_Picture()
    #context = {'expertImg': expertImg}
    context = {'expert' : expert}
    return render(request, 'experts/expert.html', context)

def topic(request, topic_id):
    experts_list = Expert.objects.order_by('-expert_Name')
    topic_object = get_object_or_404(Topic, pk=topic_id)
    context = {'experts_list' : experts_list,'topic_object' : topic_object}
    return render(request, 'experts/topic.html',context)

def news(request):
    experts_list = Expert.objects.order_by('-expert_Name')
    topics_list = Topic.objects.order_by('-topic_Name')
    news_list = News.objects.order_by('-created_at')
    news_images = News.objects.order_by('-news_Image')
    context = {'experts_list' : experts_list,'topics_list' : topics_list,'news_list' : news_list, 'news_images' : news_images}
    context_list = [experts_list, topics_list, news_list, news_images]

    #BROKEN PAGINATION
    paginator = Paginator(context_list, 4)
    page_number = request.GET.get('page')
    context_list_b = paginator.get_page(page_number)

    #This is supposed to return 6 news classes' values to the HTML
    #return render(request, 'experts/news.html', {'page_number' : page_number})
    return render(request, 'experts/news.html', context)
