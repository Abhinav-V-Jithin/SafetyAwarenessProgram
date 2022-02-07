from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Quote(models.Model):
	words  = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")

	def __str__(self):
		return f'"{self.words}", by {self.author}'

class Employer(models.Model):
	name    = models.CharField(max_length=30)
	contact = models.CharField(max_length=10)
	pc_no   = models.CharField(max_length=30, default="")
	attempts= models.IntegerField()

	def __str__(self):
		return f"PC_NO: {self.pc_no}\t Name: {self.name}"

class Prize(models.Model):
	name = models.CharField(max_length=20)
	link = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Winner(models.Model):
	employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="employers")
	prize    = models.ForeignKey(Prize, on_delete=models.CASCADE, related_name="prizes")

	def __str__(self):
		return f"{self.employer} claims a/an {self.prize}"