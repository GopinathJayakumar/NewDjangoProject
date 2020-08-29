from django.shortcuts import render
from .models import Chat


# Create your views here.
def chat_details_view(request):
    obj = Chat.objects.get(id=1)
    context = {"object": obj}
    return render(request, "details_view.html", context)


def chat_list_view(request):
    obj = Chat.objects.all()
    context = {"object_list": obj}
    for eachObj in obj:
        print(eachObj)
    return render(request, "list_view.html", context)
