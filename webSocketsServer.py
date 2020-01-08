import websockets
import os
import cv2
import numpy as np
import base64
import time
import asyncio
#from EAR_detection import * 

async def sendImage(websocket, path):
	receiverStr = await websocket.recv()
	frame = np.frombuffer(receiverStr, dtype=np.uint8)
	frame = frame.reshape(480,640,3)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#val = sleep_prediction(gray)
	message = "False"
	await websocket.send(message)

start_server = websockets.serve(sendImage, "0.0.0.0", int(os.environ['PORT_SOCKET']))
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()   
