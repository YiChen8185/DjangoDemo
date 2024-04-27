from django.urls import path
from . import views # use to find the views.py file in the same directory

# URLConf.
# Every app has its own URL configuration.
# we can save it to the home urls.py file.

urlpatterns = [
    path('hi/', views.say_hello)
    # first element is route: srting that contains URL pattern.
    # second element is view: function that will be called when URL pattern is matched.
    # It retuns an HttpResponse object.
    
    # If it adds to main, do not need playground/hi.
]