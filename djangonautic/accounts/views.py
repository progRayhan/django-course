from django.shortcuts import render

# Create your views here.
def account_number(request):
    return render(request,'accounts/account_number.html')