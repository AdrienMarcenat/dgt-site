from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from django.contrib.auth.models import User

class Article(models.Model):

    UPLOAD_TO = 'uploads/articles/thumbnail/'

    tags = models.ManyToManyField('Tag', verbose_name=_('tags'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name=_('category'))

    authors  = models.ManyToManyField(User, verbose_name=_('authors'))
    title    = models.CharField(max_length=256, verbose_name=_('title'))
    subtitle = models.CharField(max_length=256, verbose_name=_('subtitle'))
    slug     = models.SlugField(max_length=80, verbose_name=_('slug'))

    thumbnail = models.ImageField(upload_to=UPLOAD_TO, null=True,
                                  blank=True, verbose_name = _('thumbnail'))

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    pub_date = models.DateTimeField(blank=True, null=True)

    contents = models.TextField(verbose_name=_('contents'))

    def __str__(self):
        return self.title


class Tag(models.Model):

    tag = models.CharField(max_length=256, verbose_name=_('tag'))

    def __str__(self):
        return self.tag


class Category(models.Model):

    name = models.SlugField(max_length=256, default="game design",
                            verbose_name=_('category'))

    def __str__(self):
        return self.name
