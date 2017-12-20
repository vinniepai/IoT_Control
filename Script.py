import requests
import json
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
device = config.get("Device_IDs", "device")
api_key = config.get("TPLink_API_Key", "key")

url = "https://use1-wap.tplinkcloud.com?token=" + api_key

on = {
"method":"passthrough",
"params":{
"deviceId":device,
"requestData":"{\"system\":{\"set_relay_state\":{\"state\":1}}}"
}
}
off = {
"method":"passthrough",
"params":{
"deviceId":device,
"requestData":"{\"system\":{\"set_relay_state\":{\"state\":0}}}"
}
}
headers = {"Content-Type": "application/json"}

def change_state(state):
    return requests.post(url, data=json.dumps(state), headers=headers)

def user_input():
    arg = str(input("New state: "))
    on_args = ["on","turn on"]
    off_args = ["off","turn off"]
    blink_args = ["blink","blink lights"]
    exit_args = ["end","quit","exit","q"]
    if arg.lower() in on_args:
        change_state(on)
        user_input()
    elif arg.lower() in off_args:
        change_state(off)
        user_input()
    elif arg.lower() in blink_args:
        for i in range(5):
            change_state(on)
            time.sleep(1)
            change_state(off)
            time.sleep(1)
        print("End")
    elif arg.lower() in exit_args:
        quit()
    else:
        print("Error. Please enter a valid command.")
        user_input()
    return

user_input()