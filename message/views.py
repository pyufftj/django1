from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getform(request):
    if request.method=="POST":
        name=request.POST.get("name",'')
        message=request.POST.get("message",'')
        email=request.POST.get("email",'')
        address=request.POST.get("address",'')

        user_message=UserMessage(name=name,message=message,email=email,address=address)
        user_message.save()

    user_messages=UserMessage.objects.filter(name="孔平凡")
    usermessage=user_messages[0]

    return render(request, 'messageForm.html',{"myMessage":usermessage})