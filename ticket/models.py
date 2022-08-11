from django.db import models


class Role(models.Model):
	name=models.CharField(max_length=100,null=False)
	def __str__(self):
		return self.name

class Users(models.Model):
	username=models.CharField(max_length=100,null=False)
	auth_token=models.CharField(max_length=100,default=0)
	role=models.ForeignKey(Role,on_delete=models.CASCADE)

	def __str__(self):
		return self.username

class Priority(models.Model):
	name=models.CharField(max_length=100,null=False)
	def __str__(self):
		return self.name			

class Tickets(models.Model):
	title = models.CharField(max_length=30,null=False)

	status = models.CharField(max_length=30,default="open")
	description =models.CharField(max_length=100,null=False)
	priority = models.ForeignKey(Priority,on_delete=models.CASCADE)
	assignedTo=models.ForeignKey(Users,on_delete=models.CASCADE)
	createdAt=models.DateField()

	def __str__(self):
		return "%s %s %s %s %s" %(self.title,self.status,self.priority,self.priority,self.assignedTo)

