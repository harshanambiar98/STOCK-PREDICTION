from .lstm_prediction import lstm_prediction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required


# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')


@login_required(login_url="/pred_app/login/")
def index(request):
    return render(request, 'pred_app/index.html')


def pred(request):
    return render(request, 'pred_app/prediction.html')


def contact(request):
    return render(request, 'pred_app/contact.html')


def search(request, se, stock_symbol):
    import json
    predicted_result_df = lstm_prediction(se, stock_symbol)
    return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "pred_app/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "pred_app/register.html", {"form": form, "msg": msg, "success": success})


def logout_view(request):
    logout(request)
    return redirect('/pred_app/index')
# -----------------------------------------------------------
