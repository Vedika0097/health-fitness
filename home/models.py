# -*- encoding: utf-8 -*-


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

class NutritionMetrics(models.Model):

    #__NutritionMetrics_FIELDS__
    foodname = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    calories = models.IntegerField(null=True, blank=True)
    carbs = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sugar = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)

    #__NutritionMetrics_FIELDS__END

    class Meta:
        verbose_name        = _("NutritionMetrics")
        verbose_name_plural = _("NutritionMetrics")

class Dailyactivity(models.Model):

    #__Dailyactivity_FIELDS__
    activitydate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    activitytype = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    sets = models.IntegerField(null=True, blank=True)
    hours = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)

    #__Dailyactivity_FIELDS__END

    class Meta:
        verbose_name        = _("Dailyactivity")
        verbose_name_plural = _("Dailyactivity")


class Nutritionlogging(models.Model):

    #__Nutritionlogging_FIELDS__
    id = models.IntegerField(primary_key=True)
    logdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    foodname = models.ForeignKey(NutritionMetrics, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    carbs = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sugar = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)

    #__Nutritionlogging_FIELDS__END

    class Meta:
        verbose_name        = _("Nutritionlogging")
        verbose_name_plural = _("Nutritionlogging")


class Fitnessplan(models.Model):

    #__Fitnessplan_FIELDS__
    id = models.IntegerField(primary_key=True)
    caloriestoconsume = models.CharField(max_length=255, null=True, blank=True)
    caloriestoburn = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    weightLossOrGain = models.BooleanField(null=True, blank=True)

    #__Fitnessplan_FIELDS__END

    class Meta:
        verbose_name        = _("Fitnessplan")
        verbose_name_plural = _("Fitnessplan")


class Sleepmonitoring(models.Model):

    #__Sleepmonitoring_FIELDS__
    logdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    hours = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)

    #__Sleepmonitoring_FIELDS__END

    class Meta:
        verbose_name        = _("Sleepmonitoring")
        verbose_name_plural = _("Sleepmonitoring")


class FitnessDietPlan(models.Model):

    #__FitnessDietPlan_FIELDS__
    id = models.AutoField(primary_key=True)
    # foodname = models.ForeignKey(NutritionMetrics, on_delete=models.CASCADE)
    diettype = models.CharField(max_length=255, null=True, blank=True)
    # quantity = models.CharField(max_length=255, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)

    #__FitnessDietPlan_FIELDS__END

    class Meta:
        verbose_name        = _("FitnessDietPlan")
        verbose_name_plural = _("FitnessDietPlan")

#__MODELS__END
