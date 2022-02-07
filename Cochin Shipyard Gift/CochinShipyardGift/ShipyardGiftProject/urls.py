from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("QuotePage", views.QuotePage, name="QuotePage"),
	path("LoginPage", views.login_view, name="LoginPage"),
	path("LoginUser", views.login_user, name="LoginUser"),
	path("WheelPage", views.WheelPage, name="WheelPage"),
	path("LuckyNumber", views.LuckyNumber, name="LuckyNumber"),
	path("Logout", views.Logout, name="Logout"),
	path("ClaimPrize", views.ClaimPrize, name="ClaimPrize"),
]