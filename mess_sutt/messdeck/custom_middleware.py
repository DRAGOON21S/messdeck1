# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
# from allauth.socialaccount.models import SocialAccount
# class CheckUserTypeMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Code to be executed for each request before the view (and later middleware) are called.

#         response = self.get_response(request)

#         # Code to be executed for each request/response after the view is called.
#         if hasattr(request, 'user') and request.user.is_authenticated:
#             if request.user.socialaccount_set.exists(): # User authenticated using Google OAuth2
#                 return HttpResponseRedirect('http://127.0.0.1:8000/home/')
#             else: # User authenticated using username and password
#                 return HttpResponseRedirect('http://127.0.0.1:8000/home/profile')

#         return response