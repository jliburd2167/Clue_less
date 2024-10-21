# backend/messaging/views.py
from django.http import JsonResponse
from django.views import View
from .models import Message

class MessageView(View):
    def get(self, request):
        messages = Message.objects.all().order_by('-timestamp')[:50]
        return JsonResponse({'messages': [{'sender': msg.sender.username, 'content': msg.content} for msg in messages]})

    def post(self, request):
        content = request.POST['content']
        message = Message.objects.create(sender=request.user, content=content)
        return JsonResponse({'message': {'sender': message.sender.username, 'content': message.content}}, status=201)