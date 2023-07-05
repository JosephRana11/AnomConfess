from django.shortcuts import render
from .models import Message


def index_view(request):
    if request.method == 'POST':
        # Create a new Message object with the data from the POST request
        obj = Message(Sender=request.POST['SenderUserName'], Text=request.POST['SenderText'])
        
        # Save the Message object to the database
        obj.save()  
        
        print("working")  # Optional: Print a message to indicate that the code is working
        
    return render(request, 'index.html')



