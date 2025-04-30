from django.shortcuts import render, redirect
from home.forms import *
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from home.models import Dailyactivity, Nutritionlogging, NutritionMetrics
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import math
from django.db.models import Sum
from rest_framework import permissions, viewsets
from home.serializers import NutritionMetricsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request):
    user = request.user
    todayDate = datetime.today().strftime('%Y-%m-%d')
    prevDay = datetime.today() - timedelta(days=1)

    todayStepData = Dailyactivity.objects.filter(activitydate = todayDate, activitytype=5, user_id=user.id).values()
    yesterdayStepData = Dailyactivity.objects.filter(activitydate = prevDay.strftime('%Y-%m-%d'), activitytype=5, user_id=user.id).values()
    todayStep = todayStepData[0]['sets'] if len(todayStepData) > 0 else 0
    yesterdayStep = yesterdayStepData[0]['sets'] if len(yesterdayStepData) > 0 else 0
    diffStepPerc = math.floor(((todayStep-yesterdayStep)/todayStep) * 100) if todayStep > 0 else -100

    todayWkOutData = Dailyactivity.objects.filter(activitydate = todayDate, activitytype=2, user_id=user.id).values()
    yesterdayWkOutData = Dailyactivity.objects.filter(activitydate = prevDay.strftime('%Y-%m-%d'), activitytype=2, user_id=user.id).values()
    todayWkOut = todayWkOutData[0]['sets'] if len(todayWkOutData) > 0 else 0
    yesterdayWkOut = yesterdayWkOutData[0]['sets'] if len(yesterdayWkOutData) > 0 else 0
    diffWkOutPerc = math.floor(((todayWkOut-yesterdayWkOut)/todayWkOut) * 100) if todayWkOut > 0 else -100

    todayCalData = Nutritionlogging.objects.filter(logdate = todayDate, user_id=user.id).aggregate(Sum('calories'))
    yesterdayCalData = Nutritionlogging.objects.filter(logdate = prevDay.strftime('%Y-%m-%d'), user_id=user.id).aggregate(Sum('calories'))
    todayCal = todayCalData['calories__sum'] if todayCalData['calories__sum'] is not None else 0
    yesterdayCal = yesterdayCalData['calories__sum'] if yesterdayCalData['calories__sum'] is not None else 0
    diffCalPerc = math.floor(((todayCal-yesterdayCal)/todayCal) * 100) if todayCal > 0 else -100

    sleepTimeToday = Sleepmonitoring.objects.filter(logdate = todayDate, user_id=user.id).first()
    sleepTimeYstday = Sleepmonitoring.objects.filter(logdate = prevDay, user_id=user.id).first()
    sleepTimeTodayHrs = sleepTimeToday.hours if sleepTimeToday is not None else 0
    sleepTimeYstdayHrs = sleepTimeYstday.hours if sleepTimeYstday is not None else 0
    diffSleepTimePerc = math.floor(((sleepTimeTodayHrs-sleepTimeYstdayHrs)/sleepTimeTodayHrs) * 100) if sleepTimeTodayHrs > 0 else -100
    sleepLastDays = Sleepmonitoring.objects.filter(user_id=user.id).order_by("-logdate")[:7]
    sleepLabels = []
    sleepHours = []
    for sleepObj in sleepLastDays.iterator():
        sleepLabels.append(sleepObj.logdate.strftime('%d %b'))
        sleepHours.append(sleepObj.hours)

    walkStepsLastDays = Dailyactivity.objects.filter(activitytype=5, user_id=user.id).order_by("-activitydate")[:7]
    walkSteps = []
    walkDays = []
    for activity in walkStepsLastDays.iterator():
        walkDays.append(activity.activitydate.strftime('%d %b'))
        walkSteps.append(activity.sets)

    wktOutLastDays = Dailyactivity.objects.filter(activitytype=2, user_id=user.id).order_by("-activitydate")[:7]
    wktOut = []
    wktOutDays = []
    for activity in wktOutLastDays.iterator():
        wktOutDays.append(activity.activitydate.strftime('%d %b'))
        wktOut.append(activity.sets)

    context = {
        'segment': 'dashboard',
        'todayStep': todayStep,
        'diffStepPerc': diffStepPerc,
        'todayCal': todayCal,
        'diffCalPerc': diffCalPerc,
        'todayWkOut': todayWkOut,
        'diffWkOutPerc': diffWkOutPerc,
        'sleepTimeTodayHrs': sleepTimeTodayHrs,
        'diffSleepTimePerc': diffSleepTimePerc,
        'sleepLabels': sleepLabels,
        'sleepHours': sleepHours,
        'walkSteps': walkSteps,
        'walkDays': walkDays,
        'wktOut': wktOut,
        'wktOutDays': wktOutDays
    }
    return render(request, 'pages/index.html', context)

def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, 'pages/tables.html', context)


@login_required(login_url="/accounts/login/")
def dailyactivity(request):
    user = request.user
    userDailyActivity = Dailyactivity.objects.filter(user_id=user.id)

    context = {
        'segment': 'dailyactivity',
        'pageTitle': "Daily Activity",
        'activityData': userDailyActivity
    }

    return render(request, 'pages/dailyactivity.html', context)

@login_required(login_url="/accounts/login/")
def nutrition(request):
    user = request.user
    userNutritionLogging = Nutritionlogging.objects.filter(user_id=user.id)
    context = {
        'segment': 'nutrition',
        'pageTitle': "Nutrition Logging",
        'activityData': userNutritionLogging
    }
    return render(request, 'pages/nutrition.html', context)


@login_required(login_url="/accounts/login/")
def fitnessplan(request):
    isFilled = False
    if request.method == 'POST':
        existing = Fitnessplan.objects.filter(user_id=request.user.id).first()
        if(existing is not None):
           form = FitnessplanForm(request.POST, request=request, instance=existing)
           isFilled = True
        else:
            form = FitnessplanForm(request.POST, request=request)
        
        if form.is_valid():
            form.save()
            print('Fitness plan saved successfully!')
            return redirect('/fitnessplan/')
        else:
            print("Invalid fitness plan data!")
            print(form.errors)
    else:
        existing = Fitnessplan.objects.filter(user_id=request.user.id).first()
        if(existing is not None):
           form = FitnessplanForm(request=request, instance = existing)
           isFilled = True
        else:
            form = FitnessplanForm(request=request)
    
    context = {
        'form': form,
        'segment': 'fitnessplan',
        'pageTitle': "Fitness Plans",
        'isFilled': isFilled
    }
    return render(request, 'pages/fitnessplan.html', context)

    

@login_required(login_url="/accounts/login/")
def sleepmonitoring(request):
    user = request.user
    user = request.user
    sleepmonitoringData = Sleepmonitoring.objects.filter(user_id=user.id)

    context = {
        'activityData': sleepmonitoringData,
        'segment': 'sleepmonitoring',
        'pageTitle': "Sleep Monitoring"
    }
    return render(request, 'pages/sleepmonitoring.html', context)


@login_required(login_url="/accounts/login/")
def add_sleeptime(request):
    user = request.user
    if request.method == 'POST':
        form = SleepmonitoringForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            print('Sleeping target saved successfully!')
            return redirect('/sleepmonitoring/')
        else:
            print("Invalid Sleeping target data!")
    else:
        form = SleepmonitoringForm(request=request)

    context = {
        'form': form,
        'segment': 'sleepmonitoring',
        'pageTitle': "Sleep Monitoring"
    }
    return render(request, 'pages/sleepmonitoring-form.html', context)


@login_required(login_url="/accounts/login/")
def billing(request):
    context = {
        'segment': 'billing'
    }
    return render(request, 'pages/billing.html', context)

@login_required(login_url="/accounts/login/")
def virtual_reality(request):
    context = {
        'segment': 'virtual_reality'
    }
    return render(request, 'pages/virtual-reality.html', context)

@login_required(login_url="/accounts/login/")
def rtl(request):
    context = {
        'segment': 'rtl'
    }
    return render(request, 'pages/rtl.html', context)

@login_required(login_url="/accounts/login/")
def notifications(request):
    context = {
        'segment': 'notifications'
    }
    return render(request, 'pages/notifications.html', context)

@login_required(login_url="/accounts/login/")
def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'pages/profile.html', context)

@login_required(login_url="/accounts/login/")
def map(request):
    context = {
        'segment': 'map'
    }
    return render(request, 'pages/map.html', context)

@login_required(login_url="/accounts/login/")
def typography(request):
    context = {
        'segment': 'typography'
    }
    return render(request, 'pages/typography.html', context)

@login_required(login_url="/accounts/login/")
def icons(request):
    context = {
        'segment': 'icons'
    }
    return render(request, 'pages/icons.html', context)

@login_required(login_url="/accounts/login/")
def template(request):
    context = {
        'segment': 'template'
    }
    return render(request, 'pages/template.html', context)

@login_required(login_url="/accounts/login/")
def add_dailyactivity(request):
  if request.method == 'POST':
    form = DailyActivityForm(request.POST, request=request)
    if form.is_valid():
      form.save()
      print('Activity saved successfully!')
      return redirect('/dailyactivity/')
    else:
      print("Invalid activity data!")
  else:
    form = DailyActivityForm(request=request)
  
  context = {'form': form}
  return render(request, 'pages/dailyactivity-form.html', context)

@login_required(login_url="/accounts/login/")
def add_nutritionlogging(request):
  if request.method == 'POST':
    form = NutritionLoggingForm(request.POST, request=request)
    if form.is_valid():
      form.save()
      print('Nutrition data saved successfully!')
      return redirect('/nutrition/')
    else:
      print("Invalid nutrition data!")
  else:
    form = NutritionLoggingForm(request=request)
  
  context = {'form': form}
  return render(request, 'pages/nutrition-form.html', context)

class NutritionMetricsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NutritionMetrics.objects.all().order_by('foodname')
    serializer_class = NutritionMetricsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='food/details')
    def get_nutrition(self, request):
        nutritionId = request.GET.get('nutritionId')
        # nutritionId = request.query_params.get('nutritionId')

        result = NutritionMetrics.objects.filter(id = nutritionId).first()
        serializer = self.get_serializer(result, many=False)
        return Response(serializer.data)
       

class UserLoginView(auth_views.LoginView):
  template_name = 'pages/sign-in.html'
  form_class = LoginForm
  success_url = '/'

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'pages/sign-up.html', context)


class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/forgot-password.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm


class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm


def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')