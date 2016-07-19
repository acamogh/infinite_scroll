from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Theme(models.Model):
    theme_name = models.CharField(max_length=400)

    def __unicode__(self):
        return self.theme_name
