from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm, UpdateForm, DeleteForm
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

def home(request):
	return render(request,"home.html")

def insert(request, uid=1):
	if request.method =="POST":
		inform=InfoForm(request.POST)
		if inform.is_valid():
			inform.save()
			messages.info(request, "Information stored successfully")
			return redirect(reverse("employee:display"))
		else:
			messages.info(request,"Invalid Information")
			return redirect(reverse("employee:insert"))
	else:
		inform=InfoForm()
		return render(request, "insert.html",{"inform":inform})

def display(request):
	data = Info.objects.all()
	context = {'data':data}
	return render(request, 'display.html',context)

def update(request):
	if request.method =="POST":
		upform=UpdateForm(request.POST)
		if upform.is_valid():
			uid = request.POST.get('uid','')
			new_name = request.POST.get("name",'')
			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.update(name=new_name)
				messages.info(request, "Name updated successfully")
				Variable = Info.objects.all()
				print(Variable)
				return redirect(reverse("employee:display"))
			else:
				messages.info(request, "Invalid uid, not found in database")
				Variable = Info.objects.all()
				print(Variable)
				return redirect(reverse("employee:update"))
		else:
			messages.info(request, "Invalid Data")
			Variable = Info.objects.all()
			print(Variable)
			return redirect(reverse("employee:update"))
	else:
		upform=UpdateForm()
		Variable = Info.objects.all()
		print(Variable)
		
		return render(request, "update.html",{"upform":upform,'Variable':Variable})



def delete(request):
	if request.method =="POST":
		delform=DeleteForm(request.POST)
		if delform.is_valid():
			uid = request.POST.get('uid','')
			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.delete()
				messages.warning(request, "Record Deleted successfully")
				return redirect(reverse("employee:display"))
			else:
				messages.warning(request, "Invalid uid, not found in database")
				return redirect(reverse("employee:delete"))
		else:
			messages.warning(request, "Invalid Data")
			return redirect(reverse("employee:delete"))
	else:
		data = Info.objects.all()
		return render(request, "delete.html",{"data":data})