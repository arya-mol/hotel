from django.db import models

# Create your models here.

class CoursesOfMeals(models.Model):
    foodname=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    veriousfood=models.CharField(max_length=100,null=True)
    options=(
        ('dessert','dessert'),
        ('main_course','main_course'),
        ('starters','starters'),
        ('salad', 'salad'),
        ('mignardise', 'mignardise'),
    )
    status=models.CharField(max_length=150,choices=options,default='starters')





