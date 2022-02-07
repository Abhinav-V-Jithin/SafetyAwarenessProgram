from django.contrib import admin

# Register your models here.
from .models import Author, Quote, Employer, Prize, Winner

admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Employer)
admin.site.register(Prize)
admin.site.register(Winner)