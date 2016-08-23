from django.shortcuts import render

# Create your views here.
def members_list(request):
    return render(request, 'blog/members_list.html', {})