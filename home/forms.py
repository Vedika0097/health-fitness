from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from home.models import *

class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control'}),
  )
  password2 = forms.CharField(
      label=_("Password Confirmation"),
      widget=forms.PasswordInput(attrs={'class': 'form-control'}),
  )

  class Meta:
    model = User
    fields = ('username', 'email', )

    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control'
      })
    }

class DailyActivityForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(DailyActivityForm, self).__init__(*args, **kwargs)
        self.fields['activitytype'].label_from_instance = lambda instance: instance.activityname

  activitydate = forms.DateField(
      label="",
      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
  )
  activitytype = forms.ModelChoiceField(
     queryset=ActivityType.objects.all(),
     empty_label="",
     label="Activity Type",
     widget=forms.Select(attrs={'class': 'form-control'})
  )
  sets = forms.IntegerField(
      label="Total (Sets / Steps)",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  hours = forms.CharField(
      label="Hours",
      widget=forms.TextInput(attrs={'class': 'form-control'})
  )

  def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user_id = self.request.user.id
        if commit:
            instance.save()
            self.save_m2m()
        return instance

  class Meta:
    model = Dailyactivity
    fields = ('activitydate', 'activitytype', 'sets', 'hours')



class FitnessplanForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FitnessplanForm, self).__init__(*args, **kwargs)

  BOOL_CHOICES = (('', ''), (True, 'Weight Loss'), (False, 'Weight Gain'))
  height = forms.IntegerField(
      label="Height (cm)",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  weight = forms.IntegerField(
      label="Weight (kg)",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  weightLossOrGain = forms.BooleanField(
      label="Weight Loss/Gain",
      widget=forms.Select(attrs={'class': 'form-control'}, choices = BOOL_CHOICES)
  )

  def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user_id = self.request.user.id
        print(self.request.POST['weightLossOrGain'])
        if commit:
            instance.save()
            self.save_m2m()
        return instance

  class Meta:
    model = Fitnessplan
    fields = ('height', 'weight', 'weightLossOrGain')


class SleepmonitoringForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SleepmonitoringForm, self).__init__(*args, **kwargs)

  logdate = forms.DateField(
      label="",
      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
  )
  hours = forms.IntegerField(
      label="Hours",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  
  def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user_id = self.request.user.id
        if commit:
            instance.save()
            self.save_m2m()
        return instance

  class Meta:
    model = Sleepmonitoring
    fields = ('logdate', 'hours')


class NutritionLoggingForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(NutritionLoggingForm, self).__init__(*args, **kwargs)
        self.fields['foodname'].label_from_instance = lambda instance: instance.foodname

  logdate = forms.DateField(
      label="",
      widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
  )
  foodname = forms.ModelChoiceField(
     queryset=NutritionMetrics.objects.all(),
     empty_label="",
     label="Food",
     widget=forms.Select(attrs={'class': 'form-control'})
  )
  quantity = forms.IntegerField(
      label="Quantity",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  calories = forms.IntegerField(
      label="Calories",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  carbs = forms.IntegerField(
      label="Carbs",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  fat = forms.IntegerField(
      label="Fat",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  sugar = forms.IntegerField(
      label="Sugar",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  protein = forms.IntegerField(
      label="Protein",
      widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  

  def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user_id = self.request.user.id
        if commit:
            instance.save()
            self.save_m2m()
        return instance

  class Meta:
    model = Nutritionlogging
    fields = ('logdate', 'foodname', 'quantity', 'calories', 'carbs', 'fat', 'sugar', 'protein')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class UserPasswordResetForm(PasswordResetForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': 'Email'
  }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old Password'
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")