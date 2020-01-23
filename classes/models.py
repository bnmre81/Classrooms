from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	CHOICE_GENDER = (
			("M", "Male"),
			("F", "Female"),
		)
	GRADES = (
			("A", "A"),
			("B", "B"),
			("C", "C"),
			("D", "D"),
			("F", "F"),
		)
	gender = models.CharField(max_length=100, choices= CHOICE_GENDER)
	exam_grade = models.CharField(max_length=100, choices=GRADES)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


	