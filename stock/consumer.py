from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer

class TableData(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name='tableData'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self,close_code):
        pass

    async def receive(self,text_data):
        print(text_data)
        

     

