from django.shortcuts import render

# Create your views here.
def home_page(request):
  context = {'name': 'Ayush Kathariya'}

  return render(request, 'myapp/index.html', context)


def login_page(request):
  return render(request, 'myapp/login.html')


def signup_page(request):
  return render(request, 'myapp/signup.html')
