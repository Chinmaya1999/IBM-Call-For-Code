from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from .models import *
# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def contact(request):
    if(request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if(len(name)<2 or len(email)<2 or len(phone)<10 or len(content)<2):
            messages.error(request, "Please fill this form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your response has been Submitted Successfully. Thank You!")
    return render(request, 'mysite/contact.html')

def about(request):
    return render(request, 'mysite/about.html')

def search(request):
    query = request.GET['query']
    if(len(query)>50):
        allpost= Post.objects.none()
    else:
        allpostTitle = Post.objects.filter(title__icontains=query)
        allpostContent = Post.objects.filter(content__icontains=query)
        allpost = allpostTitle.union(allpostContent)
    if(allpost.count()==0):
        messages.warning(request, "Your searched item is not present in this blog.")
    else:
        messages.success(request, "We have something for you.")
    params = {'allpost': allpost, 'query' : query}
    return render(request,'mysite/search.html', params)

# API's
def handleSignup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(len(username)>10):
            messages.error(request, "Username length must be less than 10 character.")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain character or numberå.")
            return redirect('home')

        if(pass1!=pass2):
            messages.error(request, "Password not matched. Please try again")
            return redirect('home')

        myuser = User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        userinformation = Userinfo(username=username,firstname=fname,lastname=lname, email=email, password=pass1)
        userinformation.save()
        messages.success(request,"You have successfully registered in this Blog. Welcome!")
        return redirect('home')
    else:
        return HttpResponse("404 not Found")

def handleLogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']
        user = authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In. Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials. Please try again")
            return redirect('home')
    return HttpResponse("Error 404 . Login through Webapp")

def profile(request):
    if request.method=="POST":
        data=Userinfo.objects.filter(username=request.user)
        data1=User.objects.filter(username=request.user)
        fname1=request.POST['fnamea']
        lname1=request.POST['lnamea']
        phone=request.POST['phone']
        address=request.POST['address']
        pin=request.POST['pin']
        data.update(firstname=fname1,lastname=lname1,phone=phone,address=address,pin=pin)
        data1.update(first_name=fname1, last_name=lname1)
        messages.success(request, "Successfully Profile Updated")

    data=Userinfo.objects.filter(username=request.user)
    params={'data':data}
    return render(request, 'mysite/profile.html',params)

def deleteacc(request):
    if request.method=="POST":  
        try:
            u = User.objects.get(username = request.user)
            p= Userinfo.objects.get(username=request.user)
            logout(request)
            u.delete()
            p.delete()
            messages.success(request, "The user is deleted")            

        except:
            data=Userinfo.objects.filter(username=request.user)
            params={'data':data}
            return render(request, 'mysite/profile.html',params)
    
    return redirect('home')

def changepassword(request):
    if(request.method=='POST'):
        old=request.POST['old']
        new=request.POST['new']
        new1=request.POST['new1']
        data=Userinfo.objects.filter(username=request.user)
        password=data[0].password
        if(password!=old):
            messages.error(request,"Your Password is not Matching")
            d=Userinfo.objects.filter(username=request.user)
            params={'data':d}
            return render(request, 'mysite/profile.html',params)
        elif(new!=new1):
            messages.error(request,"Your new Password is not Matching")
            d=Userinfo.objects.filter(username=request.user)
            params={'data':d}
            return render(request, 'mysite/profile.html',params)
        data=Userinfo.objects.filter(username=request.user)
        data1=User.objects.filter(username=request.user)
        data.update(password=new)
        data1.set_password(new)
        messages.success(request, "Password Changed Successfully")
        params={'data':data}
        return render(request, 'mysite/profile.html',params)


def donateFood(request):
    if(request.method=='POST'):
        foodStatus = request.POST['foodStatus']
        exampleFoodDescription= request.POST['exampleFoodDescription']
        user=request.user
        donate = DonatedFood(foodStatus=foodStatus, foodDescription=exampleFoodDescription,user=user)
        donate.save()
        distributionCentres=DistributionCentre.objects.all()
        # don=DonatedFood.objects.get(donate.no)
        print('Working',donate.no)
        # messages.success(request,"Your response has been Submitted Successfully. Thank You!")
        return render(request,'mysite/selectFoodDonationCentre.html',{'centres':distributionCentres,'no':donate})

    return render(request,'mysite/donateFood.html')

def donateCloth(request):
    if(request.method=='POST'):
        clothType = request.POST.get('clothType')
        exampleClothDescription= request.POST.get('exampleClothDescription')
        user=request.user
        
        donate = DonatedCloth(clothType=clothType, clothDescription=exampleClothDescription,user=user)
        donate.save()
        distributionCentres=DistributionCentre.objects.all()
        # don=DonatedFood.objects.get(donate.no)
        print('Working',donate.no)
        # messages.success(request,"Your response has been Submitted Successfully. Thank You!")
        return render(request,'mysite/selectClothDonationCentre.html',{'centres':distributionCentres,'no':donate})
    return render(request,'mysite/donateCloth.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out. Visit after website again!. If you have any issue then post it on contact tab. Thankyou!")
    return redirect('home')

def chooseFoodCentre(request,pk,no):
    centre=DistributionCentre.objects.get(id=pk)
    
    if DonatedFood.objects.get(no=no):
        food=DonatedFood.objects.get(no=no)
        status='Pending'
        donation=foodDonation(distributionCentre=centre,donatedFood=food,status=status)
        donation.save()
        messages.success(request,"Your response has been Submitted Successfully. Thank You!")
        return redirect('home')

def chooseClothCentre(request,pk,no):
    centre=DistributionCentre.objects.get(id=pk)
    cloth=DonatedCloth.objects.get(no=no)
    status='Pending'
    donation=clothDonation(distributionCentre=centre,donatedCloth=cloth,status=status)
    donation.save()
    messages.success(request,"Your response has been Submitted Successfully. Thank You!")
    return redirect('home')


    # donatedFood=DonatedFood.objects.get(no=donate)
    # print('working',centre,status,donatedFood)





