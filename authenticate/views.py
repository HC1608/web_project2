from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm 
# Create your views here.
var = '100'
def index(request): 
	return render(request, 'authenticate/index.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('You\'re logged in'))
			return redirect('index') #routes to 'home' on successful login  
		else:
			messages.error(request,('Incorrect credentials'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('You\'re now logged out'))
	return redirect('index')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			a = form.cleaned_data.get('user_token')
			if a == var:
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username=username, password=password)
				login(request,user)
				messages.success(request, ('Youre now registered'))
				return redirect('index')
			else:	
				messages.error(request, ('Please get the registration number from owner'))
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('index')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})



def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)


def create_trip(request): 
	context = {'data':[1,2,3,4,5],'a':'str'}
	return render( request, "authenticate/create_trip.html",context)

def view_trip(request): 
	return render( request, "authenticate/view_trip.html")

def report(request): 
	return render( request, "authenticate/report.html")