from django.shortcuts import render

# Create your views here.

# landing.html을 보여준다.
def landing(request):
    return  render(
        request,
        'single_pages/landing.html'
    )
# about_me.html을 보여주도록 설정
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )