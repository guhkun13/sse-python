import asyncio
import websockets
import time

async def connect_to_server():
    async with websockets.connect('ws://localhost:8082/event') as websocket:
        # Send a message to the server
        message = "Selamat Malam Dunia!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received message from server: {response}")
        time.sleep(5)

# Run the client
# asyncio.get_event_loop().run_until_complete(connect_to_server())
asyncio.get_event_loop().run_until_complete(connect_to_server())
