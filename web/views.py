import stripe
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, TemplateView

from .models import movie_card, movie_content

# Create your views here.


class index(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loop"] = movie_card.objects.all()
        context["code"] = movie_content.objects.all()

        return context


class movie(TemplateView):
    template_name = "web/movie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loop"] = movie_card.objects.all()

        return context


class details(DetailView):
    template_name = "web/details.html"

    model = movie_card


def login_1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("signup")
    return render(request, "web/account/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            customer = User.objects.create_user(
                request, username, email, password, confirm_password
            )
            customer.save()

        return redirect("login_1")

    return render(request, "web/account/signup.html")


# def login(request):
#     return render (request, 'web/account/login.html')
# def signup(request):
#     return render(request,'web/account/signup.html')


def success(request):
    return render(request, "web/success.html")


def sorry(request):
    return render(request, "web/sorry.html")


def seat(request):
    return render(request, "web/seat.html")


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        # price = 220

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "INR",
                        "unit_amount": int(250) * 100,
                        "product_data": {"name": "ticket"},
                    },
                    "adjustable_quantity": {
                        "enabled": True,
                        "minimum": 1,
                        "maximum": 10,
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/",
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


def logout_view(request):
    logout(request)
    return render(request, "web/index.html")


from django.views.generic import TemplateView


class SuccessView(TemplateView):
    template_name = "web/payment/success.html"


class CancelView(TemplateView):
    template_name = "web/payment/cancel.html"
