from django.shortcuts import render
from Message.models import Message
from django.views.generic import ListView

class MessageBoardView(ListView):
    model = Message
    template_name = 'Messageboard.html'
    ordering = ['-pk']


