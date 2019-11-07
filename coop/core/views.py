from django.shortcuts import render


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {
                'user': request.user,
            })
    else:
        return render(request, 'cover.html')
