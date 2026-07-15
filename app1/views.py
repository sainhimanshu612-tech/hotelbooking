from django.shortcuts import render,redirect
from app1.models import Booking,userdata,contect,rooms,Review,Facility,Image
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,get_user,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
import razorpay
from django.shortcuts import get_object_or_404
import datetime 
# Create your views here.

data= datetime.datetime.now()
def index(request):
    date=data.date()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        check_in=request.POST.get("check_in")
        check_out=request.POST.get("check_out")
        guests=request.POST.get("guests")
        room_type=request.POST.get("room_type")
        message=request.POST.get(" message ")
        room_no=request.POST.get("room_no")
        
        print(name,email,phone,check_in,check_out,guests,room_type, message,room_no )
        user=Booking.objects.create(name=name,email=email,phone=phone,check_in=check_in,check_out=check_out,guests=guests,room_type=room_type,message=message,room_no=room_no )
        user.save()
        return redirect(peyment)
    return render(request,"index.html",{'date':date})

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        meassge=request.POST.get("meassge")
        print(name,email,phone,meassge)
        user=contect.objects.create(name=name,email=email,phone=phone,meassge=meassge)
        user.save()
    return render(request,"contact.html")

def gallery(request):
    return render(request,"gallery.html")

def room(request):
    rooms1 = rooms.objects.all()
    return render(request, "room.html", {"data": rooms1})

def register(request):
     if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        photo=request.FILES.get("photo")
        print(username,email,phone,password,password2,photo)
        user=userdata.objects.create_user(username=username,email=email,password=password)
        user.phone=phone
        photo = request.FILES.get("photo")
        if photo:
            user.photo = photo
        user.save()
        return redirect("login")
     return render(request,"register.html")
 
 
def login_page(request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("index")
    else:
        form=AuthenticationForm()
    return render(request,"login.html")


def logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        photo = request.FILES.get("photo")
        if photo:
            user.photo = photo
        user.save()
        return redirect("profile")
    return render(request, "edit.html")

def admindata(request):
    bookings = Booking.objects.all()
    return render(request,"admin/admindata.html",{"bookings":bookings})


def logindata(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        data =authenticate(request,username=username, password=password)
        if data is not None:

            if data.user_roll =="admin":
                login(request, data)
                return redirect(admindata)
            else:
               messages.error(request,"only for admin login")
               return redirect(logindata)
    return render(request, "admin/logindata.html",)

# def add_admin(request):
#     username="himanshu"
#     pasword="123456"
#     email="himanshu@gmail.com"
#     user=userdata.objects.create_user(username=username,password=pasword,email=email)
#     user.user_roll="admin"
#     user.save()
#     return HttpResponse("admin rgister sucssfully")

def logoutdata(request):
    logout(request)
    return redirect('logindata')

@login_required
def profiledata(request):
    return render(request, "admin/profiledata.html")

def roomdata(request):
    bookings = Booking.objects.all()
    return render(request,"admin/roomdata.html",{"bookings":bookings})

def user(request):
    bookings = Booking.objects.all()
    return render(request,"admin/userdata.html",{"bookings":bookings})

def booking(request):
    bookings = Booking.objects.all()
    return render(request,"admin/booking.html",{"bookings":bookings})

def feedback(request):
    bookings = Booking.objects.all()
    return render(request,"admin/feedback.html",{"bookings":bookings})


def roomdetail(request,id):
    data=rooms.objects.get(id=id)
    d1=data.facilities.all()
    fac1=""
    for i in d1:
        print(i.name)
        fac1=(i.description)
    images = data.images.all()
    fac1=fac1.split(",")
    if request.method == "POST":
        check_in=request.POST.get("check_in")
        check_out=request.POST.get("check_out")
        guests=request.POST.get("guests")
        name=request.POST.get("name")
        phone=request.POST.get("phone") 
        room_price=request.POST.get("room_price")
        print(check_in,check_out,guests,name,phone,room_price)
        user=Booking.objects.create(check_in=check_in,check_out=check_out,guests=guests,name=name,phone=phone,room_price=room_price)
        user.save()
        return redirect(peyment)
    return render(request,"roomdetail.html",{'data':data,"images": images,"fac1":fac1})


def peyment(request):
    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )


    payment = client.order.create({

        "amount":50000,
        "currency":"INR",

        "payment_capture":1

    })


    data={
        "payment":payment,
        "key":settings.RAZORPAY_KEY_ID
    }


 
    return render( request,"peyment.html",data)
  
       
   
def booking_edit(request,id):

    booking = get_object_or_404(Booking,id=id)


    if request.method=="POST":

        booking.name=request.POST.get("name")
        booking.email=request.POST.get("email")
        booking.phone=request.POST.get("phone")
        booking.check_in=request.POST.get("check_in")
        booking.check_out=request.POST.get("check_out")
        booking.guests=request.POST.get("guests")
        booking.room_no=request.POST.get("room_no")
        booking.message=request.POST.get("message")

        booking.save()

        return redirect("admindata")


    return render(request,"admin/edit_booking.html",
    {
        "booking":booking
    })



def booking_delete(request,id):

    booking=get_object_or_404(Booking,id=id)

    booking.delete()

    return redirect("admindata")     
       
    
    
    