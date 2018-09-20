from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('accounts/dashboard')
    else:
        return render(request, 'index.html')
def start(request):
    return render(request, 'start.html')