from django.shortcuts import render,redirect
from accounts.forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(req):
	return render(req,'home.html')

def contact(req):
	return render(req,'contact.html')

def signup(req):
	form = UserForm()
	if req.method=='POST':
		form = UserForm(req.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Done")
	return render(req,'register.html',{'form':form})

def signin(req):
	if req.method=='POST':
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(req,user)
		return redirect('signin')

	return render(req,'login.html')
	
@login_required
def signout(req):
	logout(req)
	return redirect('home')

@login_required
def profile(req):
	user = get_user(req)

	return render(req,'profile.html',{"user":user})