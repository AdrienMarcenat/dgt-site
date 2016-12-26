from django.db import models
from django.utils.translation import ugettext as _

class ArticleEntry(models.Model):

    authors  = models.ManyToManyField('User', verbose_name=_('authors'))
    title    = models.CharField(max_length=256, verbose_name=_('title'))
    subtitle = models.CharField(max_length=256, verbose_name=_('subtitle'))
    slug     = models.SlugField(max_length=80, verbose_name=_('slug'))
    
    create_date = models.DateTimeField(auto_now_add=True) 
    update_date = models.DateTimeField(auto_now=True)

    pub_date    = models.DateTimeField(blank=True, null=True)

    contents = models.TextField(verbose_name=_('contents')) 
