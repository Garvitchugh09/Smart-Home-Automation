-from firebase import firebase
import urllib.request
import http

base = "http://"ip address of NODE MCU"/"
def transfer(my_url):   #use to send and receive data
    try:
        n = urllib.request.urlopen(base + my_url).read()
        n = n.decode("utf-8")
        return n
    except http.client.HTTPException as e:
        return e

def bulb():
    bulb_action_from_mobile = fb.get("/BULB", None)
    if bulb_action_from_mobile == "ON":
        print(" TURNING THE BULB  ON")
        fb.put("/", '/BULB_ACK', "ON")                           # BULB ON ACK
        two = transfer("two")                                    # RASP CODE TO TURN ON THE BULB
    elif bulb_action_from_mobile == "OFF":
        print("TURNING THE BULB OFF")
        fb.put("/", '/BULB_ACK', "OFF")                          # BULB OFF ACK
        one = transfer("one")                                    # RASP CODE TO TURN OFF THE BULB
def fan():
    fan_action_from_mobile = fb.get("/FAN", None)
    if fan_action_from_mobile == "ON":
        print(" TURNING THE FAN  ON")
        # RASP CODE TO TURN ON THE FAN
        # FAN ON ACK
        fb.put("/", '/FAN_ACK', "ON")
    elif fan_action_from_mobile == "OFF":
        print("TURNING THE FAN OFF")
        # RASP CODE TO TURN OFF THE FAN
        # FAN OFF ACK
        fb.put("/", '/FAN_ACK', "OFF")

if __name__ == '__main__':
    fb = firebase.FirebaseApplication("Firebase link of project connected")
    while True:
        bulb()
        #fan()