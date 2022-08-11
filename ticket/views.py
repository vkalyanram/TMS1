from django.shortcuts import render
from uuid import uuid4
from .models import Users,Role,Priority,Tickets
import random
from datetime import datetime

def generate_key():
	rand_token = uuid4()
	return rand_token

def validate_user(user:str):
	try:
		users=Users.objects.get(username=user)
		return True
	except:
		return False
	
def index(request):
	roles=Role.objects.all()
	context={
	'roles':roles
	}
	return render(request,'index.html',context)

def authorize(request):
	if request.method=='POST':
		user_name= request.POST["uname"]
		role_id=request.POST["role"]
		authtoken=str(generate_key())
		flag=validate_user(user_name)
		if flag:
			message="Sorry"+" "+user_name+" "+"is already present"+" "+"Please try with another username"
		else:
			
			user_object=Users(username=user_name,role_id=role_id,auth_token=authtoken)
			user_object.save()
			message="Hi"+" "+user_name+" "+"Your token was generated :"+authtoken
		
		context={
		'message':message
		
		}
		return render(request,'status.html',context) 
	else:
		roles=Role.objects.all()
		context={
		'roles':roles
		}
		return render(request,'index.html',context)       
def raiseticket(request):
	if request.method=='POST':
		users=Users.objects.filter(role_id=1)
		to_be_assiged_users_list=[user.id for user in users]
		to_be_assiged = random.choice(to_be_assiged_users_list)
		title= request.POST["title"]
		description=request.POST["description"]
		priority=request.POST["priority"]
		tickets_object=Tickets(title=title,description=description,priority_id=priority,assignedTo_id=to_be_assiged,createdAt=datetime.now())
		#user=Users.objects.get(id=to_be_assiged)
		#Name_to=user.username
		tickets_object.save()
		message="INC0000"+str(tickets_object.id)
		context={
		'message':message
		
		}     
		return render(request,'status.html',context) 
	else:
		
		prioritys=Priority.objects.all()
		context={
		
		'prioritys':prioritys
		}
		return render(request,'ticket.html',context) 		

