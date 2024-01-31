
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record 




def record_list(request):
	rec = Record.objects.all()
	return render (request,'record_list.html',{'reco':rec})



def home(request):
    try:
        records = Record.objects.all()

        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record added successfully")
                return redirect("home")
        else:
            form = AddRecordForm()

        return render(request, 'home.html', {'records': records, 'form': form})

    except Exception as e:
        print(e)
        messages.error(request, "An error occurred.")
        return redirect('home')
   

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})






def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		
		return render(request, 'record.html', {'customer_record':customer_record})
	   
	
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')





# def update_record(request, pk):
# 	if request.user.is_authenticated:
		
# 		current_record = Record.objects.get(id=pk)
# 		form = AddRecordForm(request.POST or None, instance=current_record)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Record Has Been Updated!")
# 			return redirect('home')
# 		return render(request, 'update_record.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')
	

# def update_record(request, pk):
# 	if request.user.is_authenticated:
#         	records = Record.objects.all()
#             context={
#                 'records'=records
# 			}
# 	return redirect(request,'home.html',context)


# def update_record(request, pk):
    
# 	if request.user.is_authenticated:
# 			records = Record.objects.get(id=pk)
# 			if request.method == "POST":
# 				fname = request.POST.get("fname")
# 				lname = request.POST.get("lname")
# 				email = request.POST.get("email")
# 				phone = request.POST.get("phone")
# 				city = request.POST.get("city")
# 				address = request.POST.get("address")
# 				state = request.POST.get("state")
# 				zipcode = request.POST.get("zipcode")

# 				records.first_name = fname
# 				records.last_name = lname
# 				records.email = email
# 				records.phone = phone
# 				records.city = city
# 				records.address = address
# 				records.zipcode = zipcode
				
# 				records.save()
#                 return redirect('home')
			



def update_record(request, pk):
   if request.user.is_authenticated:
    records = Record.objects.get(id=pk)
    
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

        records.first_name = fname
        records.last_name = lname
        records.email = email
        records.phone = phone
        records.city = city
        records.address = address
        records.state = state  # Corrected indentation
        records.zipcode = zipcode
        records.save()
        messages.success(request, "sucecessfully edited data" )
        return redirect('home')

    # Handle cases where the user is not authenticated or other errors
  # Replace 'error_page.html' with the actual name or path of your error page
