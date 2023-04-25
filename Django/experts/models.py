from django.db import models
from django.db.models import Model
from django.utils.translation import gettext_lazy as _

class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic_Name = models.TextField()
    def __str__(self):
       return self.topic_Name
class Link(models.Model):
    name = models.TextField()
    url = models.URLField()
class Expert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expert_Name = models.TextField()
    expert_Picture = models.ImageField(upload_to="expertPic")
    expert_Field = models.TextField()
    class Colleges(models.TextChoices):
        ARTSSCIENCE = 'Arts and Sciences', _('Arts and Sciences')
        AGRICULTURELIFESCIENCE = 'AgricultureLifeSciences', _('Agriculture and Life Sciences')
        ARCHITECHTUREARTDESIGN = 'ArchitechtureArtDesign', _('Architechture, Art and Design')
        BUSINESS = 'Business', _('Business')
        EDUCATION = 'Education', _('Education')
        FORESTRESOURCES = 'Forest Resources', _('Forest Resources')
        VETERINARYMEDICINE = 'Veterninary Medicine', _('Veterninary Medicine')
        ENGINEERING = 'Engineering', _('James Worth Bagley College of Engineering')
        HONORS = 'ShackoulsHonors', _('Shackouls Honors College')
    expert_College = models.CharField(choices=Colleges.choices,max_length=24)
    expert_Phone = models.IntegerField()
    expert_Email = models.EmailField()
    expert_Topics = models.ManyToManyField(Topic)
    expert_Achievements = models.TextField()
    expert_Links = models.ManyToManyField(Link)
    def __str__(self):
       return self.expert_Name
    
class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_Name = models.TextField()
    news_Description = models.TextField()
    news_Image = models.ImageField(null=True, blank=True, upload_to="images/")
    news_Link = models.URLField()
    news_Link_Description = models.TextField()
    news_Expert = models.ManyToManyField(Expert)
    def __str__(self):
        return self.news_Name