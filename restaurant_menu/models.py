from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available')
)

#These are columns in a database
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)   #this is a column in a database
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    meal_type = models.CharField(max_length=500, choices = MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)      #CASCADE will delete all meals from the User who is deleted
                                                                    #PROTECT will keep all meals because the User cannot be deleted
                                                                    #SET_NULL if User is deleted, then the User will be NULL and the meals will remain
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal