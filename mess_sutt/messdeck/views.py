from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm
from .json1 import load_menu_data
from .models import Date, breakfast, lunch, dinner
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden, HttpResponse

def staff_check(user):
    return user.is_staff

def non_staff_check(user):
    return not user.is_staff


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)

def dispatch(self, request, *args, **kwargs):
  if request.user.is_authenticated:
    return redirect(to='/')
  return super(RegisterView, self).dispatch(request, *args, **kwargs)

def login(request):
    return (request, 'messdeck/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'messdeck/home.html',{
        
    })

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'messdeck/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')
        return render(request, self.template_name, {'form': form,
    })


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='messdeck-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'messdeck/profile.html', {'user_form': user_form, 'profile_form': profile_form})


# @method_decorator(user_passes_test(staff_check), name='dispatch')
@login_required
def load_data(request):
    if staff_check(request.user):
        if request.method == 'POST':
            load_menu_data()
            return render(request, 'messdeck/menu_load.html', {'message': 'Data loaded successfully.'})
        else:
            return render(request, 'messdeck/menu_load.html')
    else:
        return HttpResponseForbidden()

#import json as json

# def load_menu_data():
#     with open('messdeck/mess menu/asdf.json') as f :
#         data= json.load(f)

    # for date, date_dict in data.items():
    #     breakfast_items = date_dict["BREAKFAST"]
    #     print(f"{date:}")
    #     for item in breakfast_items:
    #         print(f"{item}")

from .forms import BKrating

@login_required
def viewmenu(request):
    dates = Date.objects.all()
    breakfasts = breakfast.objects.all()
    lunchs = lunch.objects.all()
    dinners= dinner.objects.all()
    context = {'dates': dates, 'breakfasts': breakfasts,
               'lunchs': lunchs, 'dinners': dinners}
    return render(request, 'messdeck/menu.html', context)
    # if request.method == 'POST':
    #     form = BKrating(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Your rating is submitted successfully')
    #         return render(request, 'messdeck/menu.html', {'form': form},context)
    #     else:
    #         messages.error(request, 'Invalid submission')
    #         return render(request, 'messdeck/menu.html', {'form': form},context)
    # else:
    #     form = BKrating()
    #     return render(request, 'messdeck/menu.html', {'form': form},context)

    
    


from .models import Feedback
from .forms import FeedbackForm

# @method_decorator(user_passes_test(non_staff_check))
@login_required
def feedback(request):
    if non_staff_check(request.user):
        if request.method == 'POST':
            form = FeedbackForm(request.POST, request.FILES)
            if form.is_valid():
                feedback_ = form.save(commit=False)
                feedback_.user = request.user
                feedback_.save()
                messages.success(request, 'Your feedback is submitted successfully')
                return redirect('feedback')
                # return redirect('feedback_success')
        else:
            form = FeedbackForm()

        return render(request, 'messdeck/feedback.html', {'form': form})
    else:
        return HttpResponseForbidden()

# @method_decorator(user_passes_test(non_staff_check), name='dispatch')
# def feedback_success(request):
#     return render(request, 'messdeck/feedback_success.html')


@login_required
def viewfeedback(request):
    if staff_check(request.user):
        feedbacks = Feedback.objects.all()
        return render(request, 'messdeck/viewfeedback.html', {'feedbacks': feedbacks})
    else:
        return HttpResponseForbidden()


# if request.method == 'POST':
#         form = BreakfastForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseForbidden("Submission successful.")
#         else:
#             return HttpResponseForbidden("Invalid submission.")
#     else:
#         form = BreakfastForm()
#         return render(request, 'submit_breakfast.html', {'form': form})

import datetime

# def mealperiod(hour):
#     return 'breakfast'
    # if 7 <= hour < 9 or 12 <= hour < 15 or 19 <= hour < 21:
    #     if 7 <= hour < 9:
    #         return 'breakfast' 
    #     elif 12 <= hour < 14:
    #         return 'lunch' 
    #     else :
    #         return 'dinner'
    # return None


from .models import attend
from .forms import BKattendance, LHattendance, DNattendance

@login_required
def markattendance(request):
    currenttime = datetime.datetime.now()
    hour = currenttime.hour
    #student = attend.objects.get_or_create(user=request.user)
    if  7 <= hour < 9: # and not student.has_attended_breakfast:
        if request.method == 'POST':
            BKattend = BKattendance(request.POST, instance=request.user)

            if BKattend.is_valid() :
                bk_attend=BKattend.cleaned_data.get('BKattend')
                if bk_attend:
                    attend.has_attended_breakfast = True
                    attend.save()
                messages.success(request, 'Your attendance is marked')
                return redirect(to='attendance')
        else:
            BKattend = BKattendance(instance=request.user)
            return render(request, 'messdeck/attendance.html', {'BKattend': BKattend})
        
    elif 12<= hour < 15:
        if request.method == 'POST':
            LHattend = LHattendance(request.POST, instance=request.user)

            if LHattend.is_valid() :
                lh_attend=LHattend.cleaned_data.get('has_attended_lunch')
                if lh_attend:
                    attend.has_attended_lunch = True
                    attend.save()
                messages.success(request, 'Your attendance is marked')
                return redirect(to='attendance')
        else:
            LHattend = LHattendance(instance=request.user)
            return render(request, 'messdeck/attendance.html', {'LHattend': LHattend})
        
    elif 19<= hour < 21:
        if request.method == 'POST':
            DNattend = DNattendance(request.POST, instance=request.user)

            if DNattend.is_valid() :
                dn_attend=DNattend.cleaned_data.get('has_attended_dinner')
                if dn_attend:
                    attend.has_attended_dinner = True
                    attend.save()
                messages.success(request, 'Your attendance is marked')
                return redirect(to='attendance')
        else:
            DNattend = DNattendance(instance=request.user)
            return render(request, 'messdeck/attendance.html', {'DNattend': DNattend})
    # elif 12 <= hour < 16 and not student.has_attended_lunch:
    #     student.has_attended_lunch = True
    #     student.save()
    #     return HttpResponse("Your attendance has been marked for lunch.")

    # elif 20 <= hour < 23 and not student.has_attended_dinner:
    #     student.has_attended_dinner = True
    #     student.save()
    #     return HttpResponse("Your attendance has been marked for dinner.")
    else:
        return HttpResponse("Attendance marking is not available at this time.")


    # return HttpResponse("You have already marked your student for this meal period.")
# if mealperiod is None:
#         return HttpResponse("Attendance marking is not available at this time.")
