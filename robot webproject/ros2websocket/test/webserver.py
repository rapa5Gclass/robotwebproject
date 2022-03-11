########################
# Server

import asyncio              # 웹 소켓 모듈을 선언한다.
import websockets           # 클라이언트 접속이 되면 호출된다.

import json

ready = 0

def batterytext():
    f = open("/tmp/batteryper.txt", 'r')
    data = f.readline()
    f.close()
    return(data)

def linXtext():
    f = open("/tmp/cmdx.txt", 'r')
    data = f.readline()
    f.close()
    return(data)

def angZtext():
    f = open("/tmp/cmdz.txt", 'r')
    data = f.readline()
    f.close()
    return(data)

async def accept(websocket, path):

    while True:
        clinetData = await websocket.recv()
        battery_data = batterytext()
        x_data = linXtext()
        z_data = angZtext()
        targetData = {
            "robot_id": "rapa1",
            "battery_percentage" : battery_data,
            "linear_x": x_data,
            "angular_z" : z_data
        }
        jsonTargetData = json.dumps(targetData)
        await websocket.send(jsonTargetData)


start_server = websockets.serve(accept, "", 9988)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()