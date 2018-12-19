from django.shortcuts import render,redirect
from .models import Items
from .forms import ItemsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.utils import timezone
from .models import userComments
from .forms import userCommentsForm

def Ecomhome(request):
	print(request.session.get("first_name"))
	return render(request, "Ecomhome.html", {})

def contgect_page(request):
	if request.method == 'POST':
		form = userCommentsForm(request.POST or None)
		if form.is_valid():
			print("form validation")
			form.save()
			return render(request, "contact_page.html", {})

	else:
		user_comments = userComments.objects.all
		return render(request, "contact_page.html", {'all_user':user_comments})


	

def JohnOrder(request):
	 key = request.session.session_key
	 #print(key)
	 request.session['first_name']="Sumesh"
	 items_all = Items.objects.all()
	 page = request.GET.get('page', 2)
	 paginator = Paginator(items_all, 3)
	 now = timezone.now()
	 print(now)
	 try:
	 	items = paginator.page(page)
	 except PageNotAnInteger:
	 	items = paginator.page(1)
	 except EmptyPage:
	 	items = paginator.page(paginator.num_pages)
	 return render(request, "JohnOrder.html", { 'items': items })

