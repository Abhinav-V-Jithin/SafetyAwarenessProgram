from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Quote, Employer, Prize, Winner
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import reverse
import random

# Create your views here.
def index(request):
	return render(request, "ShipyardGiftProject/index.html")

def login_view(request):
	if not request.user.is_authenticated:
		return render(request, "ShipyardGiftProject/login.html")
	return HttpResponseRedirect(reverse("QuotePage"))
	
def login_user(request):
	username = str(request.POST["username"])
	phone_number = str(request.POST["phone_number"])
	pc_no = str(request.POST["pc_no"])
	user = authenticate(request, username=username, password=pc_no)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("LoginPage"))
	e=None
	e2=None
	u=None
	u2=None
	try:
		e = Employer.objects.get(pc_no=pc_no)
	except:
		pass
	try:
		e2= Employer.objects.get(name=username)
	except:
		pass
	try:
		u = User.objects.get(password=pc_no)
	except:
		pass
	try:
		u2= User.objects.get(name=username)
	except:
		pass
	if u is not None:
		if u.username != username or u.pc_no != pc_no:
			context = {
					"message" : "Invalid username for the PC number",
			}

			return render(request, "ShipyardGiftProject/Error.html", context)
	if u2 is not None:
		if u2.username != username or u2.pc_no != pc_no:
			context = {
					"message" : "Invalid username for the PC number",
			}

			return render(request, "ShipyardGiftProject/Error.html", context)
	if e is not None:
		if username != e.name or pc_no != e.pc_no:
			context = {
				"message" : "Invalid username for the PC number",
			}

			return render(request, "ShipyardGiftProject/Error.html", context)
	if e2 is not None:
		if e2.name != username or e2.pc_no != pc_no:
			context = {
					"message" : "Invalid username for the PC number",
			}

			return render(request, "ShipyardGiftProject/Error.html", context)
	employer = Employer(name=username, contact=phone_number, attempts=0, pc_no = pc_no)
	employer.save()

	
	user = User.objects.create_user(username=username, password=pc_no)
	user.save()

	login(request, user)
	return HttpResponseRedirect(reverse("LoginPage"))
	
	

def QuotePage(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("LoginPage"))
	employer = Employer.objects.get(name=request.user.username)

	if employer.attempts >= 3:
		context = {
			"message" : "Oops! You have exceeded your attempts...Have a good day!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)
	e = None
	try:
		e = Winner.objects.get(employer=employer)
	except Winner.DoesNotExist:
		e = None

	if e is not None:
		context = {
			"message" : "Oops! You have already won your price!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)

	quotes = Quote.objects.all()

	quote = random.choice(quotes)

	context = {
		"name" : quote.author.name,
		"words": quote.words,
	}

	return render(request, "ShipyardGiftProject/QuotePage.html", context)

def WheelPage(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("LoginPage"))

	employer = Employer.objects.get(name=request.user.username)

	if employer.attempts >= 3:
		context = {
			"message" : "Oops! You have exceeded your attempts...Have a good day!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)
	e = None
	try:
		e = Winner.objects.get(employer=employer)
	except Winner.DoesNotExist:
		e = None

	if e is not None:
		context = {
			"message" : "Oops! You have already won your price!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)

	context = {
		"result":None,
	}
	return render(request, "ShipyardGiftProject/Wheel.html", context)

def LuckyNumber(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("LoginPage"))

	employer = Employer.objects.get(name=request.user.username)
	num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	result = 0

	if num == 10:
		result = 1

	context = {
		"result": result,
	}
	if employer.attempts >= 3:
		context = {
			"message" : "Oops! You have exceeded your attempts...\nHave a good day!"
		}
		return render(request, "ShipyardGiftProject/Error.html", context)
	e = None
	try:
		e = Winner.objects.get(employer=employer)
	except Winner.DoesNotExist:
		e = None
	if e is not None:
		context = {
			"message" : "Oops! You have already won your price!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)
	employer = Employer.objects.get(name=request.user.username)
	employer.attempts += 1
	employer.save()

	return render(request, "ShipyardGiftProject/Wheel.html", context)

def ClaimPrize(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("LoginPage"))

	prize = random.choice(Prize.objects.all())

	context = {
		"name" : prize.name,
		"link": prize.link,
	}
	e = None
	try:
		employer = Employer.objects.get(name=request.user.username)
		e = Winner.objects.get(employer=employer)
	except Winner.DoesNotExist:
		e = None
	if e is not None:
		context = {
			"message" : "Oops! You have already won your price!",
		}
		return render(request, "ShipyardGiftProject/Error.html", context)

	Winner(employer=Employer.objects.get(name=request.user.username), prize = prize).save()


	return render(request, "ShipyardGiftProject/Prize.html", context)


def Logout(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("LoginPage"))
	logout(request)
	return HttpResponseRedirect(reverse("index"))