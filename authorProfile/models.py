from django.db import models
from django.utils.translation import ugettext as _

from article.models import User

class AuthorProfile(models.Model):
    
    user = models.ForeignKey('article.User', default="", on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_('description'))
    
    def __str__(self):
        return self.user.firstname + self.user.lastname
