from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.

class contect (models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    meassge=models.TextField()
    
class userdata(AbstractUser):
    phone=models.CharField(max_length=12)
    photo=models.ImageField(upload_to="photo/",blank=True,null=True)
    roll=(
        ('Admin',"admin"),
        ("Customber","customber")
    )
    user_roll=models.CharField(choices=roll,default="Customer",null=True,max_length=10)
    
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class rooms(models.Model) :
    room_no=models.IntegerField()  
    ROOM_CHOICES = [
        ("Single Room", "Single Room"),
        ("Double Room", "Double Room"),
        ("Deluxe Room", "Deluxe Room"),
        ("Suite Room", "Suite Room"),
    ]  
    room_type = models.CharField(max_length=50, choices=ROOM_CHOICES) 
    room_price=models.IntegerField() 
    room_capacity=models.CharField(max_length=10)
    availibility_status=models.BooleanField()
    facilities = models.ManyToManyField(Facility, blank=True)
    description = models.TextField(blank=True, null=True) 


class Booking(models.Model):
    room=models,models.ForeignKey(rooms, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    room_no = models.IntegerField(null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    room_price=models.ImageField()
    GUEST_CHOICES = [
        ("1 Guest", "1 Guest"),
        ("2 Guests", "2 Guests"),
        ("3 Guests", "3 Guests"),
        ("4 Guests", "4 Guests"),
    ]

    guests = models.CharField(max_length=20, choices=GUEST_CHOICES)

    ROOM_CHOICES = [
        ("Single Room", "Single Room"),
        ("Double Room", "Double Room"),
        ("Deluxe Room", "Deluxe Room"),
        ("Suite Room", "Suite Room"),
    ]

    room_type = models.CharField(max_length=50, choices=ROOM_CHOICES)

    message = models.TextField(blank=True, null=True)

    booking_date = models.DateTimeField(auto_now_add=True)



class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
  
    
class Review(models.Model):
    review_id = models.CharField(max_length=100)
    user = models.ForeignKey("userdata", on_delete=models.CASCADE)
    hotel_id = models.CharField(max_length=100)
    rating = models.IntegerField()  # 1 to 5 stars
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
class Image(models.Model):
    room = models.ForeignKey(rooms, on_delete=models.CASCADE, related_name="images")
    photo = models.ImageField(upload_to="room_image/")