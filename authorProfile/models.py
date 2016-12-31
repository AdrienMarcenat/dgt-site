from django.db import models
from django.utils.translation import ugettext as _

class AuthorProfile(models.Model):
    
    firstname = models.CharField(max_length=256, verbose_name=_('firstname'))
    lastname  = models.CharField(max_length=256, verbose_name=_('lastname'))
    
    description = models.TextField(verbose_name=_('description'))
    
    def __str__(self):
        return self.lastname
