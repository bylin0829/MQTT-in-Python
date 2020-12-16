import paho.mqtt.client as mqtt
import requests

# class mymqtt():
#     def __init__():
#         pass

#     def connect():
#         print("Start to connect MQTT server.")
    
#     def publish():
#         pass

def mqtt_publish(ip):
    print("mqtt_publish:execute->in")
    # User information
    user_account = ""   #Setting
    user_password = ""  #Setting
    
    # Execute mqtt publish
    client = mqtt.Client()
    client.username_pw_set(user_account, user_password)
    client.connect(ip, 1883, 60)

    topic = "hum_tmp"
    payload = '{ \"timestamp\": 111, \"temperature\": 3.141, \"humidity\": 2.1, \"location\": \"taipei\"}'
    client.publish(topic=topic,payload=payload)
    client.disconnect()
    print("mqtt_publish:execute->out")

def get_ip():
    print("get_ip->execute:in")
    api_url = "" #Setting
    response = requests.post(api_url)
    print(f"api response status:{response.status_code}")
    if response.status_code == 200:
        text = response.json()
        print(f"ip:{text['IP']}")
        print("get_ip->execute:out")
        return text['IP']
    else:
        print("Call api failure.")
        print("get_ip->execute:out")
        return

if __name__ == "__main__":
    # mqtt_publish()
    ip = get_ip()
    mqtt_publish(ip)