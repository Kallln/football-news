from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406436000',
        'name' : 'Ahmad Haikal Najmuddin',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)


