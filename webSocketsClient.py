import cv2
import websockets
import numpy as np
import base64
import time
import asyncio

async def readImage():
	uri = "ws://192.168.0.105:30000"
	cap = cv2.VideoCapture(0)
	async with websockets.connect(uri) as websocket:
		_, img = cap.read()
		img = cv2.resize(img, (640,480))
		img = np.array(img, dtype = np.uint8).reshape(1, 640*480*3)
		img_text = bytearray(img)
		await websocket.send(img_text)

asyncio.get_event_loop().run_until_complete(readImage())
	

