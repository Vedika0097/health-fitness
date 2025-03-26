# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class ActivityType(models.Model):

    #__ActivityType_FIELDS__
    activityname = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(primary_key=True)

    #__ActivityType_FIELDS__END

    class Meta:
        verbose_name        = _("ActivityType")
        verbose_name_plural = _("ActivityType")

class Dailyactivity(models.Model):

    #__Dailyactivity_FIELDS__
    activitydate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    activitytype = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    sets = models.IntegerField(null=True, blank=True)
    hours = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(primary_key=True)

    #__Dailyactivity_FIELDS__END

    class Meta:
        verbose_name        = _("Dailyactivity")
        verbose_name_plural = _("Dailyactivity")


class Nutritionlogging(models.Model):

    #__Nutritionlogging_FIELDS__
    id = models.IntegerField(primary_key=True)
    foodname = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)

    #__Nutritionlogging_FIELDS__END

    class Meta:
        verbose_name        = _("Nutritionlogging")
        verbose_name_plural = _("Nutritionlogging")


class Fitnessplan(models.Model):

    #__Fitnessplan_FIELDS__
    id = models.IntegerField(primary_key=True)
    caloriestoconsume = models.CharField(max_length=255, null=True, blank=True)
    caloriestoburn = models.CharField(max_length=255, null=True, blank=True)
    carbs = models.CharField(max_length=255, null=True, blank=True)
    protein = models.CharField(max_length=255, null=True, blank=True)
    fat = models.CharField(max_length=255, null=True, blank=True)
    sugar = models.CharField(max_length=255, null=True, blank=True)

    #__Fitnessplan_FIELDS__END

    class Meta:
        verbose_name        = _("Fitnessplan")
        verbose_name_plural = _("Fitnessplan")


class Sleepmonitoring(models.Model):

    #__Sleepmonitoring_FIELDS__
    hours = models.CharField(max_length=255, null=True, blank=True)

    #__Sleepmonitoring_FIELDS__END

    class Meta:
        verbose_name        = _("Sleepmonitoring")
        verbose_name_plural = _("Sleepmonitoring")



#__MODELS__END
