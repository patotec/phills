from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from .forms import *
from django.contrib import messages
import string
import random
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

def myindex(request):
	title = 'Home'
	qs = Review.objects.all()
	if request.method == 'POST':
		track_id = request.POST.get('id')
		try:
			fillid = Quote.objects.get(track_id=track_id)		
			messages.success(request, 'Data Fetched Successfully')
		except:
			fillid = None
			messages.error(request, 'Invalid ID')
		context = {'data':fillid}
		return render(request, 'index/far.html', context=context)
		
	context = {'title':title,'frt':qs}
	return render(request,'index/index.html',context)


def myabout(request):
	title = 'About'
	context = {'title':title}
	return render(request,'index/about-us.html',context)


def myservices(request):
	title = 'Services'
	context = {'title':title}
	return render(request,'index/fleet.html',context)


def mycontact(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			return redirect('indexurl:contact')
	else:
		form = Contactform()
	title = 'Contact-us'
	context = {'title':title}
	return render(request,'index/contact.html',context)

def mytrack(request):
	title = 'Track'
	if request.method == 'POST':
		track_id = request.POST.get('id')
		fillid = Quote.objects.filter(track_id=track_id)
		if fillid.exists():
			qs = Quote.objects.get(track_id=track_id)
			context = {'data':qs}
			return render(request,'index/far.html',context)
		else:
			messages.error(request, 'invalid ID')
	context = {'title':title}
	return render(request,'index/track.html',context)

def myquote(request):
	if request.method == 'POST':
		fullname = request.POST.get('name')
		email = request.POST.get('email')
		type_shipment = request.POST.get('type')
		destination = request.POST.get('destination')
		pickup = request.POST.get('pickup')
		width = request.POST.get('width')
		height = request.POST.get('height')
		length = request.POST.get('length')
		weight = request.POST.get('weight')
		date_at = request.POST.get('date')
		filtername = Quote.objects.filter(fullname=fullname)
		if filtername.exists():
			messages.error(request, 'name already in use')
		else:
			randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
			create = Quote.objects.create(fullname=fullname,email=email,type_shipment=type_shipment,destination=destination,pickup=pickup,width=width,height=height,length=length,weight=weight,track_id=randompin,date_at=date_at)
			email_body = render_to_string('index/mil.html', {
			'data':create
			})
			msg = EmailMultiAlternatives(subject='Track ID', body=email_body, from_email=settings.DEFAULT_FROM_EMAIL,to=[email] )
			msg.attach_alternative(email_body, "text/html")
			msg.send()
			messages.success(request,'order created successfully')

	title = 'Quote'

	# if request.method == 'POST':
	# 	track_id = request.POST.get('id')
	# 	if track_id:
	# 		try:
	# 			fillid = Quote.objects.get(track_id=track_id)		
	# 			messages.success(request, 'Data Fetched Successfully')
	# 		except:
	# 			fillid = None
	# 			messages.error(request, 'Invalid ID')
	# 		context = {'fillid':fillid}
	# 		return render(request, 'index/track-response.html', context=context)
		

	context = {'title':title}
	return render(request, 'index/quote.html',context)


def dash(request):
	# qs=Quote.objects.get()
	# context = {'data':qs}
	return render(request, 'index/faq.html')