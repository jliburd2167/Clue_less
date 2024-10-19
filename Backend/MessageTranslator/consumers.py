import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the notifications group
        self.channel_layer = get_channel_layer()  # Get the channel layer
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the notifications group
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def notify(self, event):
        # Send notification to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
                    'message': message
                }
            )
        )
