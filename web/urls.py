from django.contrib import admin
from django.urls import path
from . import views
from . views import index, details, movie
from .views import CreateStripeCheckoutSessionView

from .views import CancelView, SuccessView
app_name='web'

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('details/<int:pk>',details.as_view(),name="details"),
    path("login",views.login_1,name="login"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),

    path('movie',movie.as_view(),name="movie"),

    
    

    path("seat",views.seat,name="seat"),
    path("signup",views.signup,name="signup"),
    path("success",views.success,name="success"),
    path("sorry",views.sorry,name="sorry"),
    path("logout",views.logout_view,name='logout'),  

    path("create-checkout-session/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",)
]
