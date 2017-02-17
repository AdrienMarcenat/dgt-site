from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class AuthorProfile(models.Model):

    user = models.ForeignKey(User, verbose_name=_('author'))
    description = models.TextField(verbose_name=_('description'))

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
