from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from django.template import Template, RequestContext
from django import template
from django.template import Context
from django.http import QueryDict
import requests
from authen.models import User



mac_id_hashtable={}


def user_registration(request):

	if(request.method=='POST'):
		import ipdb;ipdb.set_trace()
		data = json.loads(request.body)
		ip_address=get_client_ip(request)
		print data['mac_address']
		print data['name']
		u=User.objects.create(mac_id=data['mac_address'],ip_address=ip_address,first_name=data['name'],email=data['email'],roll_no= ['roll_no'],password=data['password'],college_name=data['college_name'])
		print 'Done'
		print User.objects.all()
		return HttpResponse("SUCCESS")
	else:
		return HttpResponse("Failed")


def make_hash():
	all_entries = Entry.objects.all()
	global mac_id_hashtable
	
	for user in all_entries:
		mac_id=user.mac_id
		mac_id_hashtable[mac_id]=1

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def checkValidEmail(request):
	data=json.loads(request.body)
	if data.has_key('emailid'):
		emailid=data['emailid']
		num_results = User.objects.filter(email=emailid).count()
		if num_results==0:
			return HttpResponse("True")
		else:
			return HttpResponse("False")
	else:
		return HttpResponse("no email recieved")

def logincheck(request):
	data=json.loads(request.body)
	if data.has_key('email') and data.has_key('password'):
		tempname=data['email']
		num_results = User.objects.filter(email=tempname).count()
		if num_results!=0:			
			temp=User.objects.get(email=tempname)
			print temp
			temppass=data['password']
			if temppass==temp.password:
				return HttpResponse("True")
			else:
				return HttpResponse("False")
		else:
			return HttpResponse("user is not registered")
	else:
		return HttpResponse("enter both entries")