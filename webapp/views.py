from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from webapp.forms import loginForm,studentForm
from django.contrib.auth.decorators import login_required
from webapp.models import student


# Create your views here.


# Student


def view(request, pk):
    data = student.objects.get(id=pk)
    return render(request, 'view.html', {'data': data})


def delete(request, pk):
    data=student.objects.get(id=pk)
    data.delete()
    return redirect('index')

def update(request, pk):
    # select * from student where id=pk
    data = student.objects.get(id=pk)
    form = studentForm(instance=data) #Attach data to formfield
    if request.method == "POST":
        form = studentForm(request.POST,instance=data)
        if form.is_valid():
            #form.save()
            stu=student()
            stu.id=pk
            stu.first_name=form.cleaned_data['first_name']
            stu.middle_name=form.cleaned_data['middle_name']
            stu.last_name=form.cleaned_data['last_name']
            stu.email=form.cleaned_data['email']
            stu.address=form.cleaned_data['address']
            stu.gender = form.cleaned_data['gender']
            stu.is_active = form.cleaned_data['is_active']
            stu.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

#Create form

#@login_required(login_url='/signin')
def create(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            #form.save()
            stu=student()
            # stu.name=form.cleaned_data['email'].split('@')[0]
            stu.first_name=form.cleaned_data['first_name']
            stu.middle_name=form.cleaned_data['middle_name']
            stu.last_name=form.cleaned_data['last_name']
            stu.email=form.cleaned_data['email']
            stu.address=form.cleaned_data['address']
            stu.gender = form.cleaned_data['gender']
            stu.is_active = form.cleaned_data['is_active']
            stu.save()
            return redirect('index')
    return render(request,'create.html',{'form':form})

#@login_required(login_url='/signin')
def index(request):
    #select * from student
    data=student.objects.all().order_by('first_name')
    return render(request,'index.html',{'data':data})


# End Of Student

def Signup(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    form= UserCreationForm()
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=User()
            user.username=form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request,'Signup.html',{'form':form,'msg':'Registration done successfully'})
    return render(request,'Signup.html',{'form':form ,'msg':''})

def Signin(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    form=loginForm()
    if request.method == 'POST':
        form=loginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user =authenticate(username=username ,password=password)
            if user is None:
                return render(request, 'Signin.html', {'form': form, 'msg': 'No user Found'})
            else:
                login(request,user)
                request.session['city'] ='Bangalore'
                request.session['uid'] =user.id
                return redirect('dashBoard')
    return render(request,'Signin.html',{'form':form ,'msg':''})

#@login_required(login_url='/signin')
def dashBoard(request):
    if request.user.is_authenticated:
        return render(request, 'Dashboard.html')
    else:
        return redirect('Signin')
def Signout(request):
    logout(request)
    #del request.session['city']
    for k in request.session.keys():
        del request.session[k]
    return redirect('Signin')